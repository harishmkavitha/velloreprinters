/* Vellore Printers — progressive enhancement only. Content works without JS. */
(function () {
  "use strict";
  var WA = "919092833701"; // TODO: replace with the real Vellore Printers WhatsApp number

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

  /* footer year */
  var y = document.getElementById("year");
  if (y) y.textContent = new Date().getFullYear();
})();
