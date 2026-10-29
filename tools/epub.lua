-- Pandoc filter giving the EPUB the same numbering and box titles as the PDF.

local chapter = 0
local chapter_label = 0
local appendix = false
local manual_chapters = false
local appendix_chapter = 0
local structural_refs = {}
local sections = {}
local exnum = {}      -- label -> "c.n"
local count = 0
local fignum = {}     -- label -> "c.n"
local figcount = 0
local eqnum = {}      -- label -> "c.n", numbered equations (all of them carry a \label)
local eqcount = 0
local exname_of = {}  -- exercise label -> "Exercise" or "Problem"

local function optarg(blocks)
  -- Remove a leading OPTARG marker (from tools/epub_prep.py) and return its content.
  local para = blocks[1]
  if not para or para.t ~= "Para" then return nil end
  for i, el in ipairs(para.content) do
    if el.t == "Strong" and el.content[1] and el.content[1].t == "Str"
       and el.content[1].text:sub(1, 7) == "OPTARG:" then
      local inl = el.content:clone()
      inl[1] = pandoc.Str(inl[1].text:sub(8))
      if inl[1].text == "" then inl:remove(1) end
      para.content:remove(i)
      return inl
    end
  end
  return nil
end

local function label_of(blocks)
  local para = blocks[1]
  if not para or para.t ~= "Para" then return nil end
  for _, el in ipairs(para.content) do
    if el.t == "Span" and el.attributes.label then return el.attributes.label end
  end
end

local function title_para(cls, inlines)
  return pandoc.Div({ pandoc.Para(inlines) }, pandoc.Attr("", { cls .. "-title" }))
end

local function number_pass(doc)
  for i, b in ipairs(doc.blocks) do
    if b.t == "Div" and b.classes:includes("ocappendices") then
      appendix = true
    elseif b.t == "Div" and b.classes:includes("occhaptercounter") then
      chapter = assert(tonumber(pandoc.utils.stringify(b.content)), "Invalid chapter counter")
      chapter_label = chapter
      manual_chapters = true
    elseif b.t == "Header" and b.level == 1 and not b.classes:includes("unnumbered") then
      chapter = chapter + 1
      chapter_label = chapter
      if appendix then
        appendix_chapter = appendix_chapter + 1
        chapter_label = string.char(64 + appendix_chapter)
        sections = {}
        structural_refs[b.identifier] = chapter_label
        b.classes:insert("unnumbered")
        b.content:insert(1, pandoc.Str("Appendix " .. chapter_label .. ": "))
      elseif manual_chapters then
        sections = {}
        structural_refs[b.identifier] = tostring(chapter_label)
        b.classes:insert("unnumbered")
        b.content:insert(1, pandoc.Str(chapter_label .. " "))
      end
      count = 0
      figcount = 0
      eqcount = 0
    elseif (appendix or manual_chapters) and b.t == "Header" and b.level > 1 and not b.classes:includes("unnumbered") then
      local level = b.level
      sections[level] = (sections[level] or 0) + 1
      for deeper = level + 1, 6 do sections[deeper] = nil end
      local n = chapter_label
      for depth = 2, level do n = n .. "." .. (sections[depth] or 0) end
      structural_refs[b.identifier] = n
      b.classes:insert("unnumbered")
      b.content:insert(1, pandoc.Str(n .. " "))
    elseif b.t == "Div" and b.classes:includes("exercise") then
      count = count + 1
      local l = label_of(b.content)
      local n = chapter_label .. "." .. count
      b.attributes["number"] = n
      if l then
        exnum[l] = n
        exname_of[l] = b.attributes["exname"] or "Exercise"
      end
    end
    if (appendix or manual_chapters) and b.t == "Div" then
      local numbered = {theorem=true, proposition=true, lemma=true, corollary=true, definition=true, example=true}
      for _, cls in ipairs(b.classes) do
        if numbered[cls] then
          local title = b.content[1] and b.content[1].content[1]
          if title and title.t == "Strong" then
            local value = pandoc.utils.stringify(title.content)
            local n = value:match("(%d+%.%d+)$")
            if n then
              n = n:gsub("^%d+", chapter_label)
              structural_refs[b.identifier] = n
              title.content = {pandoc.Str(value:gsub("%d+%.%d+$", n))}
            end
          end
        end
      end
    end
    if b.t ~= "Header" then
      -- A display with a \label is a numbered equation: show its number as a \tag, as in the PDF.
      b = b:walk({ Math = function(m)
        local l = m.mathtype == "DisplayMath" and m.text:match("\\label{([^}]*)}")
        if not l then return nil end
        eqcount = eqcount + 1
        eqnum[l] = chapter_label .. "." .. eqcount
        if chapter_label == 0 then eqnum[l] = tostring(eqcount) end
        m.text = m.text:gsub("\\label{[^}]*}", "", 1)
        if FORMAT:match("html") then  -- the online reader (KaTeX)
          m.text = m.text .. "\\tag{" .. eqnum[l] .. "}"
          return pandoc.Span({ m }, pandoc.Attr(l))
        end
        -- The EPUB's MathML drops \tag, so the number follows the display.
        return pandoc.Span({ m, pandoc.Span({ pandoc.Str("(" .. eqnum[l] .. ")") }, pandoc.Attr("", { "eqno" })) },
                           pandoc.Attr(l))
      end })
      doc.blocks[i] = b
    end
    if b.t == "Figure" then
      figcount = figcount + 1
      local n = chapter_label .. "." .. figcount
      -- book.cls omits the chapter prefix for figures in Chapter 0.
      if chapter_label == 0 then n = tostring(figcount) end
      b.attributes["number"] = n
      if b.identifier ~= "" then fignum[b.identifier] = n end
    end
  end
end

-- Unnumbered theorem-like environments (\newtheorem*): pandoc numbers them anyway; drop the number.
local unnumbered = { remark = true, theoremx = true, propositionx = true, lemmax = true,
                     corollaryx = true, definitionx = true, examplex = true }

local function rewrite(b)
  if b.t ~= "Div" then return nil end
  if b.classes:includes("ocimagealt") then
    local description = pandoc.utils.stringify(b.content[1])
    b.content:remove(1)
    b = b:walk({ Image = function(img)
      img.caption = { pandoc.Str(description) }
      return img
    end })
    return b.content
  end
  if b.classes:includes("ocappendices") or b.classes:includes("occhaptercounter") then return {} end
  for _, cls in ipairs(b.classes) do
    if unnumbered[cls] then
      local para = b.content[1]
      local first = para and para.content and para.content[1]
      if first and first.t == "Strong" then
        first.content = pandoc.Inlines({ pandoc.Str((pandoc.utils.stringify(first.content):gsub("%s*[%d%.]+$", ""))) })
        para.content[1] = first
      end
      return b
    end
  end
  if b.classes:includes("exercise") then
    local level = optarg(b.content)
    local name = b.attributes["exname"] or "Exercise"
    local t = pandoc.Inlines({ pandoc.Strong({ pandoc.Str(name .. " " .. b.attributes["number"]) }) })
    local l = label_of(b.content)
    if level then
      t:insert(pandoc.Space())
      t:insert(pandoc.Emph(pandoc.Inlines({ pandoc.Str("(") }) .. level .. pandoc.Inlines({ pandoc.Str(")") })))
    end
    b.content:insert(1, title_para("exercise", t))
    if l then
      b.identifier = l
      -- The exercise owns this anchor. Pandoc also emits an empty Span for
      -- \label; keeping both gives duplicate IDs in EPUB and online HTML.
      b = b:walk({ Span = function(el)
        if el.attributes.label == l and el.identifier == l then
          return el.content
        end
      end })
    end
    return b
  elseif b.classes:includes("reminder") then
    local arg = optarg(b.content)
    local t = pandoc.Inlines({ pandoc.Strong({ pandoc.Str("Reminder") }) })
    if arg then t = t .. pandoc.Inlines({ pandoc.Str(": ") }) .. arg end
    b.content:insert(1, title_para("reminder", t))
    return b
  elseif b.classes:includes("beauty") then
    b.content:insert(1, title_para("beauty", { pandoc.Strong({ pandoc.Str("Why this is beautiful") }) }))
    return b
  elseif b.classes:includes("think") then
    b.content:insert(1, title_para("think", { pandoc.Strong({ pandoc.Str("Pause and think") }) }))
    return b
  elseif b.classes:includes("challenge") then
    b.content:insert(1, title_para("challenge", { pandoc.Strong({ pandoc.Str("Challenges") }) }))
    return b
  elseif b.classes:includes("solution") or b.classes:includes("hint") then
    local para = b.content[1]
    local first = para and para.content[1]
    if first and first.t == "Span" and first.content[1] then
      local l = pandoc.utils.stringify(first.content)
      local n = exnum[l] or l
      local name = exname_of[l] or "Exercise"
      local what = b.classes:includes("hint") and ("Hint for " .. name .. " ") or ("Solution of " .. name .. " ")
      para.content[1] = pandoc.Link({ pandoc.Strong({ pandoc.Str(what .. n .. ".") }) }, "#" .. l)
    end
    return b
  end
end

local function number_figure(b)
  local n = b.attributes["number"]
  if not n then return nil end
  -- The LaTeX figure caption explains the picture; include that explanation
  -- for readers who cannot see the SVG. Keep any explicitly supplied alt text.
  local description = pandoc.utils.stringify(b.caption.long)
  b = b:walk({ Image = function(img)
    local alternative = pandoc.utils.stringify(img.caption)
    if (alternative == "" or alternative == "image") and description ~= "" then
      img.caption = { pandoc.Str(description) }
      return img
    end
  end })
  local cap = b.caption.long[1]
  if cap and (cap.t == "Plain" or cap.t == "Para") then
    cap.content:insert(1, pandoc.Strong({ pandoc.Str("Figure " .. n .. ".") }))
    cap.content:insert(2, pandoc.Space())
  end
  return b
end

local function fix_ref(el)
  local eq = eqnum[el.attributes["reference"]]
  if eq then
    el.content = { pandoc.Str(el.attributes["reference-type"] == "eqref" and "(" .. eq .. ")" or eq) }
    el.target = "#" .. el.attributes["reference"]
    return el
  end
  if el.attributes["reference-type"] == "ref" then
    local n = exnum[el.attributes["reference"]] or fignum[el.attributes["reference"]] or structural_refs[el.attributes["reference"]]
    if n then
      el.content = { pandoc.Str(n) }
      el.target = "#" .. el.attributes["reference"]
      return el
    end
  end
end

function Pandoc(doc)
  -- A book may call its exercises otherwise. The marker may change mid-book,
  -- so each exercise keeps the name in force where it appears.
  local current = "Exercise"
  local kept = pandoc.Blocks({})
  for _, b in ipairs(doc.blocks) do
    if b.t == "Div" and b.classes:includes("exname") then
      current = pandoc.utils.stringify(b.content)
    else
      if b.t == "Div" and b.classes:includes("exercise") then
        b.attributes["exname"] = current
      end
      kept:insert(b)
    end
  end
  doc.blocks = kept
  number_pass(doc)
  doc = doc:walk({ Div = rewrite, Figure = number_figure })
  doc = doc:walk({ Link = fix_ref })
  -- LaTeX reader bookkeeping is not an HTML attribute. Preserve any genuine
  -- anchor, but do not emit the invalid `label` attribute on its Span.
  doc = doc:walk({ Span = function(el)
    if el.attributes.label then
      el.attributes.label = nil
      return el
    end
  end })
  return doc
end
