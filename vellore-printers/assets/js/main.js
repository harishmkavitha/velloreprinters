/* Vellore Printers — progressive enhancement only. Content works without JS. */
(function () {
  "use strict";
  var WA = "917825075552"; // Vellore Printers WhatsApp number

  /* mobile nav */
  var toggle = document.querySelector(".nav__toggle");
  var list = document.getElementById("nav-list");
  if (toggle && list) {
    toggle.addEventListener("click", function () {
      var open = list.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
    list.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", function () {
        list.classList.remove("is-open");
        toggle.setAttribute("aria-expanded", "false");
      });
    });
  }

  /* scroll reveal */
  var reveals = document.querySelectorAll(".reveal");
  if (reveals.length && "IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); }
      });
    }, { threshold: 0.12, rootMargin: "0px 0px -40px 0px" });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add("in"); });
  }

  /* contact form -> WhatsApp (no backend) */
  var form = document.getElementById("quote-form");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var status = document.getElementById("form-status");
      var val = function (n) { return (form[n] && form[n].value || "").trim(); };
      var name = val("name"), phone = val("phone");
      if (!name || !phone) {
        if (status) { status.dataset.state = "error"; status.textContent = "Please add your name and phone number so we can reply."; }
        return;
      }
      var lines = ["Hi Vellore Printers, I'd like a quote.", "", "Name: " + name, "Phone: " + phone];
      if (val("email")) lines.push("Email: " + val("email"));
      if (val("service")) lines.push("Service: " + val("service"));
      if (val("details")) lines.push("Details: " + val("details"));
      var url = "https://wa.me/" + WA + "?text=" + encodeURIComponent(lines.join("\n"));
      if (status) { status.dataset.state = "ok"; status.textContent = "Opening WhatsApp with your enquiry…"; }
      window.open(url, "_blank", "noopener");
    });
  }

  /* gallery: category filter + lightbox */
  var gallery = document.getElementById("gallery");
  if (gallery) {
    var chips = gallery.querySelectorAll(".chip");
    var cards = gallery.querySelectorAll(".gcard");
    var empty = gallery.querySelector(".gallery-empty");
    chips.forEach(function (chip) {
      chip.addEventListener("click", function () {
        chips.forEach(function (c) { c.classList.remove("is-active"); c.setAttribute("aria-pressed", "false"); });
        chip.classList.add("is-active"); chip.setAttribute("aria-pressed", "true");
        var f = chip.getAttribute("data-filter"), shown = 0;
        cards.forEach(function (card) {
          var ok = f === "all" || card.getAttribute("data-cat") === f;
          card.hidden = !ok; if (ok) shown++;
        });
        if (empty) empty.hidden = shown !== 0;
      });
    });

    var lb = document.getElementById("lightbox");
    if (lb) {
      var lbImg = lb.querySelector("img"), lbCap = lb.querySelector(".lightbox__cap");
      var open = function (src, cap) {
        lbImg.src = src; lbImg.alt = cap || ""; if (lbCap) lbCap.textContent = cap || "";
        lb.classList.add("open"); lb.setAttribute("aria-hidden", "false");
      };
      var close = function () { lb.classList.remove("open"); lb.setAttribute("aria-hidden", "true"); lbImg.src = ""; };
      cards.forEach(function (card) {
        card.addEventListener("click", function () {
          var img = card.querySelector("img");
          open(img.getAttribute("data-full") || img.src, card.getAttribute("data-cap") || img.alt);
        });
      });
      lb.addEventListener("click", function (e) { if (e.target === lb || e.target.classList.contains("lightbox__close")) close(); });
      document.addEventListener("keydown", function (e) { if (e.key === "Escape") close(); });
    }
  }

  /* footer year */
  var y = document.getElementById("year");
  if (y) y.textContent = new Date().getFullYear();
})();
