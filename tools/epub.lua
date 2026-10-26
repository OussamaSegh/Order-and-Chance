-- Pandoc filter giving the EPUB the same numbering and box titles as the PDF.

local chapter = 0
local exnum = {}      -- label -> "c.n"
local count = 0
local fignum = {}     -- label -> "c.n"
local figcount = 0
local exname = "Exercise"  -- what the book calls its exercises

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
  for _, b in ipairs(doc.blocks) do
    if b.t == "Header" and b.level == 1 and not b.classes:includes("unnumbered") then
      chapter = chapter + 1
      count = 0
      figcount = 0
    elseif b.t == "Div" and b.classes:includes("exercise") then
      count = count + 1
      local l = label_of(b.content)
      local n = chapter .. "." .. count
      b.attributes["number"] = n
      if l then exnum[l] = n end
    elseif b.t == "Figure" then
      figcount = figcount + 1
      local n = chapter .. "." .. figcount
      b.attributes["number"] = n
      if b.identifier ~= "" then fignum[b.identifier] = n end
    end
  end
end

local function rewrite(b)
  if b.t ~= "Div" then return nil end
  if b.classes:includes("exercise") then
    local level = optarg(b.content)
    local t = pandoc.Inlines({ pandoc.Strong({ pandoc.Str(exname .. " " .. b.attributes["number"]) }) })
    local l = label_of(b.content)
    if level then
      t:insert(pandoc.Space())
      t:insert(pandoc.Emph(pandoc.Inlines({ pandoc.Str("(") }) .. level .. pandoc.Inlines({ pandoc.Str(")") })))
    end
    b.content:insert(1, title_para("exercise", t))
    if l then b.identifier = l end
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
  elseif b.classes:includes("solution") or b.classes:includes("hint") then
    local para = b.content[1]
    local first = para and para.content[1]
    if first and first.t == "Span" and first.content[1] then
      local l = pandoc.utils.stringify(first.content)
      local n = exnum[l] or l
      local what = b.classes:includes("hint") and ("Hint for " .. exname .. " ") or ("Solution of " .. exname .. " ")
      para.content[1] = pandoc.Link({ pandoc.Strong({ pandoc.Str(what .. n .. ".") }) }, "#" .. l)
    end
    return b
  end
end

local function number_figure(b)
  local n = b.attributes["number"]
  if not n then return nil end
  local cap = b.caption.long[1]
  if cap and (cap.t == "Plain" or cap.t == "Para") then
    cap.content:insert(1, pandoc.Strong({ pandoc.Str("Figure " .. n .. ".") }))
    cap.content:insert(2, pandoc.Space())
  end
  return b
end

local function fix_ref(el)
  if el.attributes["reference-type"] == "ref" then
    local n = exnum[el.attributes["reference"]] or fignum[el.attributes["reference"]]
    if n then
      el.content = { pandoc.Str(n) }
      el.target = "#" .. el.attributes["reference"]
      return el
    end
  end
end

function Pandoc(doc)
  -- A book may call its exercises otherwise (marker made by tools/epub_prep.py).
  local kept = pandoc.Blocks({})
  for _, b in ipairs(doc.blocks) do
    if b.t == "Div" and b.classes:includes("exname") then
      exname = pandoc.utils.stringify(b.content)
    else
      kept:insert(b)
    end
  end
  doc.blocks = kept
  number_pass(doc)
  doc = doc:walk({ Div = rewrite, Figure = number_figure })
  doc = doc:walk({ Link = fix_ref })
  return doc
end
