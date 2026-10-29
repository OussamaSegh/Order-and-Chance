// Online reader of a volume (tools/reader.py): mathematics, menu, theme, hidden hints and solutions.
(function () {
  var root = document.documentElement, body = document.body;

  // Mathematics, typeset with KaTeX; a formula KaTeX cannot read is shown as TeX source.
  document.querySelectorAll("span.math").forEach(function (el) {
    try {
      // KaTeX cannot read a prime after a space, as in \hat f\,'.
      katex.render(el.textContent.replace(/\\([,;:!]) *'/g, "\\$1{}'"), el, { displayMode: el.classList.contains("display"), throwOnError: false,
                                         strict: false, trust: false });
    } catch (e) { el.classList.add("math-error"); }
  });
  // An inline formula wider than the screen (it cannot break inside \left...\right) scrolls sideways.
  var width = document.querySelector("main").clientWidth;
  document.querySelectorAll("span.math.inline").forEach(function (el) {
    if (el.getBoundingClientRect().width > width - 40) el.classList.add("wide");
  });

  // Light / dark switch, remembered on this device; by default the phone's own setting.
  document.getElementById("theme").addEventListener("click", function () {
    var dark = root.dataset.theme ? root.dataset.theme === "dark"
                                  : matchMedia("(prefers-color-scheme: dark)").matches;
    root.dataset.theme = dark ? "light" : "dark";
    try { localStorage.setItem("theme", root.dataset.theme); } catch (e) {}
  });

  // Table of contents drawer on small screens.
  var menu = document.getElementById("menu");
  function setMenu(open) { body.classList.toggle("menu-open", open); menu.setAttribute("aria-expanded", open); }
  menu.addEventListener("click", function () { setMenu(!body.classList.contains("menu-open")); });
  document.getElementById("shade").addEventListener("click", function () { setMenu(false); });
  document.querySelectorAll("#side a").forEach(function (a) { a.addEventListener("click", function () { setMenu(false); }); });

  // Highlight the current chapter in the sidebar and unfold its sections.
  var page = location.pathname.split("/").pop() || "index.html";
  document.querySelectorAll("#side nav a").forEach(function (a) {
    var href = a.getAttribute("href");
    if (href === page) {
      a.classList.add("current");
      for (var li = a.parentElement; li && li.tagName === "LI"; li = li.parentElement.parentElement) li.classList.add("open");
      if (window.innerWidth >= 1100) a.scrollIntoView({ block: "center" });
    }
  });

  // Hints and solutions stay folded until the reader asks: try the exercise first.
  document.querySelectorAll("div.hint, div.solution").forEach(function (div) {
    var first = div.querySelector("p strong");
    var details = document.createElement("details");
    details.className = "reveal";
    var summary = document.createElement("summary");
    summary.textContent = first ? first.textContent.replace(/\.$/, "") : (div.classList.contains("hint") ? "Hint" : "Solution");
    details.appendChild(summary);
    div.parentNode.insertBefore(details, div);
    details.appendChild(div);
  });
  // A link to something inside a folded solution opens it.
  function openTarget() {
    var id = decodeURIComponent(location.hash.slice(1)), el = id && document.getElementById(id);
    for (; el; el = el.parentElement) if (el.tagName === "DETAILS") el.open = true;
  }
  window.addEventListener("hashchange", openTarget);
  openTarget();
})();
