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
      b.classes:insert("oc-chapter")
      if appendix then b.classes:insert("oc-appendix") end
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
        b.content:insert(1, pandoc.Space())
        b.content:insert(1, pandoc.Span({ pandoc.Str(tostring(chapter_label)) }, pandoc.Attr("", { "header-section-number" })))
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
      b.content:insert(1, pandoc.Space())
      b.content:insert(1, pandoc.Span({ pandoc.Str(n) }, pandoc.Attr("", { "header-section-number" })))
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

-- ---------------------------------------------------------------- design 5e
-- docs/design/interior.md: labels are Fira capitals with a coral number, theorem notes
-- EB Garamond italic, formal statements upright; tools/epub.css and tools/reader.css
-- style the classes made here.

local formal = { theorem = true, proposition = true, lemma = true, corollary = true, definition = true,
                 example = true, theoremx = true, propositionx = true, lemmax = true, corollaryx = true,
                 definitionx = true, examplex = true }

local function label(name, number)
  local t = pandoc.Inlines({ pandoc.Span({ pandoc.Str(name) }, pandoc.Attr("", { "oc-label" })) })
  if number and number ~= "" then
    t:insert(pandoc.Space())
    t:insert(pandoc.Span({ pandoc.Str(number) }, pandoc.Attr("", { "oc-num" })))
  end
  return t
end

-- "Theorem 3.2" -> label and number; "Pause and think" -> label only.
local function split_label(text)
  local name, number = text:match("^(.-)%s+([%w%.]*%d[%w%.]*)$")
  if name and name ~= "" then return name, (number:gsub("%.$", "")) end
  return (text:gsub("[%.:]$", "")), nil
end

local function trim_inlines(inl)
  while #inl > 0 and (inl[1].t == "Space" or inl[1].t == "SoftBreak") do inl:remove(1) end
  while #inl > 0 and (inl[#inl].t == "Space" or inl[#inl].t == "SoftBreak") do inl:remove(#inl) end
  return inl
end

-- The note of a theorem, "(Fermat, $p$ prime).": without the parentheses and the full stop.
local function strip_note(inl)
  inl = trim_inlines(inl)
  if #inl == 0 then return inl end
  local first, last = inl[1], inl[#inl]
  if last.t == "Str" then
    last.text = last.text:gsub("%.$", "")
    if last.text == "" then inl:remove(#inl); last = inl[#inl] end
  end
  if first and first.t == "Str" and first.text:sub(1, 1) == "(" and last and last.t == "Str"
     and last.text:sub(-1) == ")" then
    first.text = first.text:sub(2)
    last.text = last.text:sub(1, -2)
    if first.text == "" then inl:remove(1) end
    if #inl > 0 and inl[#inl].t == "Str" and inl[#inl].text == "" then inl:remove(#inl) end
  end
  return trim_inlines(inl)
end

-- Formal boxes: a label paragraph head (label, coral number, italic note) and an upright statement.
local function style_formal(b)
  for i, para in ipairs(b.content) do
    if para.t == "Para" or para.t == "Plain" then
      local inl = para.content
      if i == 1 and inl[1] and inl[1].t == "Strong" then
        local name, number = split_label(pandoc.utils.stringify(inl[1].content))
        local head = label(name, number)
        local rest = pandoc.Inlines({})
        for k = 2, #inl do rest:insert(inl[k]) end
        -- The note runs up to the statement, which pandoc sets as one Emph.
        local note, body, seen = pandoc.Inlines({}), pandoc.Inlines({}), false
        for _, el in ipairs(rest) do
          if not seen and el.t == "Emph" then seen = true end
          if seen then body:insert(el) else note:insert(el) end
        end
        if not seen then
          local first = trim_inlines(note:clone())[1]
          if not (first and first.t == "Str" and first.text:sub(1, 1) == "(") then
            body, note = note, pandoc.Inlines({})
          end
        end
        note = strip_note(note)
        if #note > 0 then
          head:insert(pandoc.Space())
          head:insert(pandoc.Span(note, pandoc.Attr("", { "oc-note" })))
        end
        local title = pandoc.Span(head, pandoc.Attr("", { "oc-head" }))
        body = trim_inlines(body)
        if #body > 0 and body[1].t == "Str" and body[1].text == "." then body:remove(1) end
        para.content = pandoc.Inlines({ title, pandoc.Space() }) .. trim_inlines(body)
        inl = para.content
      end
      para.content = inl
    end
  end
  -- Pandoc italicises theorem statements (each paragraph or list item is one Emph);
  -- the design keeps them upright. A word emphasised in the source stays an inner Emph.
  local function upright(blk)
    local out = pandoc.Inlines({})
    for _, el in ipairs(blk.content) do
      if el.t == "Emph" then out:extend(el.content) else out:insert(el) end
    end
    blk.content = out
    return blk
  end
  return b:walk({ Para = upright, Plain = upright })
end

-- A teaching box title made by this filter: Strong "Exercise 3.2" (+ difficulty) -> label.
local function style_title(div)
  local para = div.content[1]
  if not para or not para.content or not para.content[1] or para.content[1].t ~= "Strong" then return div end
  local text = pandoc.utils.stringify(para.content[1].content)
  local name, number = split_label(text)
  local head = label(name, number)
  local rest = pandoc.Inlines({})
  for k = 2, #para.content do rest:insert(para.content[k]) end
  rest = trim_inlines(rest)
  if #rest > 0 and rest[1].t == "Str" and rest[1].text:sub(1, 1) == ":" then
    rest[1].text = rest[1].text:sub(2):gsub("^%s+", "")
    if rest[1].text == "" then rest:remove(1) end
    rest = trim_inlines(rest)
  end
  if #rest > 0 then
    head:insert(pandoc.Space())
    head:insert(pandoc.Span(rest, pandoc.Attr("", { "oc-note" })))
  end
  para.content = head
  return div
end

local function roman(n)
  local values = { { 10, "X" }, { 9, "IX" }, { 5, "V" }, { 4, "IV" }, { 1, "I" } }
  local s = ""
  for _, v in ipairs(values) do while n >= v[1] do s = s .. v[2]; n = n - v[1] end end
  return s
end

-- Pandoc's identifiers, so part pages keep the file names of earlier builds.
local function slug(inlines)
  local s = pandoc.utils.stringify(inlines):lower()
  s = s:gsub("[^%w%s%-_%.]", ""):gsub("%s+", "-"):gsub("^[^%a]+", "")
  return s ~= "" and s or "part"
end

-- Volume line, motif and parts (markers from tools/epub_prep.py), then the openers.
local function openers(doc)
  local volume, motif, parts = nil, nil, 0
  local blocks = pandoc.Blocks({})
  for _, b in ipairs(doc.blocks) do
    if b.t == "Div" and b.classes:includes("ocvolume") then
      volume = pandoc.utils.stringify(b.content)
    elseif b.t == "Div" and b.classes:includes("ocmotif") then
      b:walk({ Image = function(img) motif = img.src end })
    elseif b.t == "Div" and (b.classes:includes("ocpart") or b.classes:includes("ocpartstar")) then
      local title = b.content[1] and b.content[1].content or pandoc.Inlines({})
      local h = pandoc.Header(1, title, pandoc.Attr("part-" .. slug(title), { "oc-part", "unnumbered" }))
      if b.classes:includes("ocpart") then
        parts = parts + 1
        h.content:insert(1, pandoc.Space())
        h.content:insert(1, pandoc.Span({ pandoc.Str(roman(parts)) }, pandoc.Attr("", { "header-section-number" })))
      end
      if volume then h.attributes["masthead"] = volume end
      blocks:insert(h)
    else
      blocks:insert(b)
    end
  end
  local out = pandoc.Blocks({})
  local i = 1
  while i <= #blocks do
    local b = blocks[i]
    out:insert(b)
    if b.t == "Header" and b.level == 1 and b.classes:includes("oc-chapter") then
      if volume then b.attributes["masthead"] = volume end
      local panel = pandoc.Blocks({})
      -- The chapter's epigraph: a centred italic block directly after the title.
      local nxt = blocks[i + 1]
      if nxt and nxt.t == "Div" and nxt.classes:includes("center") then
        panel:insert(pandoc.Div(nxt.content, pandoc.Attr("", { "oc-epigraph" })))
        i = i + 1
      end
      if motif then
        panel:insert(pandoc.Div({ pandoc.Plain({ pandoc.Image({}, motif, "", pandoc.Attr("", {}, { alt = "", role = "presentation" })) }) }, pandoc.Attr("", { "oc-motif" })))
      end
      if #panel > 0 then out:insert(pandoc.Div(panel, pandoc.Attr("", { "oc-opener" }))) end
    end
    i = i + 1
  end
  doc.blocks = out
  return doc
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
    -- Design 5e: the label FIGURE in Fira capitals with a coral number, as in the PDF.
    cap.content:insert(1, pandoc.Span(label("Figure", n), pandoc.Attr("", { "oc-head" })))
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
  doc = openers(doc)
  doc = doc:walk({ Div = rewrite, Figure = number_figure })
  doc = doc:walk({ Div = function(b)
    for _, cls in ipairs(b.classes) do
      if formal[cls] then return style_formal(b) end
    end
    for _, cls in ipairs({ "exercise-title", "reminder-title", "beauty-title", "think-title", "challenge-title" }) do
      if b.classes:includes(cls) then return style_title(b) end
    end
    if b.classes:includes("remark") then
      local para = b.content[1]
      if para and para.content and para.content[1] and para.content[1].t == "Strong" then
        para.content[1] = pandoc.Span(label(pandoc.utils.stringify(para.content[1].content):gsub("%.$", ""), nil),
                                      pandoc.Attr("", { "oc-head" }))
      end
      return b
    end
    if b.classes:includes("solution") or b.classes:includes("hint") then
      local para = b.content[1]
      local link = para and para.content and para.content[1]
      if link and link.t == "Link" then
        local name, number = split_label(pandoc.utils.stringify(link.content))
        link.content = label(name, number)
        para.content[1] = pandoc.Span({ link }, pandoc.Attr("", { "oc-head" }))
      end
      return b
    end
    if b.classes:includes("proof") then
      -- The end-of-proof mark is the coral diamond of the PDF.
      return b:walk({ Str = function(s)
        if s.text:find("\u{25FB}", 1, true) then
          local text = s.text:gsub("\u{A0}\u{25FB}", ""):gsub("\u{25FB}", "")
          return { pandoc.Str(text), pandoc.Span({}, pandoc.Attr("", { "oc-qed" })) }
        end
      end })
    end
  end })
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
