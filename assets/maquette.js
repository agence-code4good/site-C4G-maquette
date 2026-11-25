// Maquette Code4Good : menu déroulant « Secteurs d'activité » et menu mobile
(function () {
  var btn = document.querySelector("[data-mega-btn]");
  var mega = document.getElementById("mega");
  var nav = document.getElementById("nav");
  var burger = document.querySelector("[data-burger]");
  var desktop = window.matchMedia("(min-width: 981px)");
  var closeTimer;

  function setOpen(open) {
    if (!btn || !mega) return;
    btn.setAttribute("aria-expanded", open ? "true" : "false");
    mega.hidden = !open;
  }

  function showPanel(key) {
    document.querySelectorAll("[data-panel]").forEach(function (p) { p.hidden = p.dataset.panel !== key; });
    document.querySelectorAll("[data-entry]").forEach(function (a) { a.classList.toggle("active", a.dataset.entry === key); });
  }

  if (btn && mega) {
    btn.addEventListener("click", function () { setOpen(btn.getAttribute("aria-expanded") !== "true"); });
    var zone = btn.parentElement;
    zone.addEventListener("mouseenter", function () { if (desktop.matches) { clearTimeout(closeTimer); setOpen(true); } });
    zone.addEventListener("mouseleave", function () { if (desktop.matches) { closeTimer = setTimeout(function () { setOpen(false); }, 180); } });
    document.querySelectorAll("[data-entry]").forEach(function (a) {
      a.addEventListener("mouseenter", function () { showPanel(a.dataset.entry); });
      a.addEventListener("focus", function () { showPanel(a.dataset.entry); });
    });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape") setOpen(false); });
    document.addEventListener("click", function (e) { if (desktop.matches && !zone.contains(e.target)) setOpen(false); });
  }

  if (burger && nav) {
    burger.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      burger.setAttribute("aria-expanded", open ? "true" : "false");
      burger.textContent = open ? "Fermer" : "Menu";
    });
  }

  // Liens vers des pages pas encore rédigées dans la maquette
  document.querySelectorAll("a.soon").forEach(function (a) {
    a.addEventListener("click", function (e) {
      e.preventDefault();
      var t = document.getElementById("toast");
      if (!t) return;
      t.hidden = false;
      clearTimeout(t._h);
      t._h = setTimeout(function () { t.hidden = true; }, 2600);
    });
  });
})();
