/* Heart To Home site scripts.
   To add photos: put the image in /images and add a line to PHOTOS.
   To add reviews: add an entry to REVIEWS (real customer reviews only). */
var PHOTOS = [
  { src: "images/wall-room.jpg", cat: "Kitchens", caption: "Kitchen install: natural maple shaker cabinets, quartz island and LVP flooring" },
  { src: "images/kitchen-b-after-2.jpg", cat: "Kitchens", stage: "After", caption: "Kitchen remodel: new cabinets, quartz island with shiplap panel" },
  { src: "images/kitchen-b-after-1.jpg", cat: "Kitchens", stage: "After", caption: "Kitchen remodel: white shaker cabinets and plank flooring" },
  { src: "images/kitchen-a-before-1.jpg", cat: "Kitchens", stage: "Before", caption: "Kitchen remodel: before" },
  { src: "images/kitchen-a-before-2.jpg", cat: "Kitchens", stage: "Before", caption: "Kitchen remodel: before, old counters and flooring" },
  { src: "images/exterior-a-after-1.jpg", cat: "Painting", stage: "After", caption: "Exterior repaint: stucco, trim and garage doors" },
  { src: "images/exterior-a-after-2.jpg", cat: "Painting", stage: "After", caption: "Exterior repaint: front entry" },
  { src: "images/exterior-a-progress.jpg", cat: "Painting", stage: "Prep", caption: "Windows, stone and lights fully masked before spraying" },
  { src: "images/exterior-a-before.jpg", cat: "Painting", stage: "Before", caption: "Exterior repaint: before" },
  { src: "images/exterior-b-after.jpg", cat: "Painting", stage: "After", caption: "Exterior repaint with contrast trim" },
  { src: "images/exterior-b-before.jpg", cat: "Painting", stage: "Before", caption: "Exterior repaint: before" },
  { src: "images/interior-accent-wall.jpg", cat: "Painting", caption: "Interior repaint with dark accent wall and built-in niches" },
  { src: "images/fireplace-wall-finished.jpg", cat: "Trim", stage: "After", caption: "Shiplap fireplace and TV wall with wood mantel" },
  { src: "images/fireplace-wall-framing.jpg", cat: "Trim", stage: "Before", caption: "Fireplace wall: framing stage" },
  { src: "images/flooring-after.jpg", cat: "Flooring", stage: "After", caption: "LVP flooring over a new-construction slab" },
  { src: "images/flooring-before.jpg", cat: "Flooring", stage: "Before", caption: "Flooring: bare slab before install" },
];
var REVIEWS = [
  // { name: "First name L.", city: "Surprise", stars: 5, text: "Review text exactly as the customer wrote it.", source: "Google" },
];
var PLACEHOLDERS = [
  ["Painting", "Interior repaint"], ["Bathrooms", "Tub-to-shower conversion"], ["Kitchens", "Kitchen install"],
  ["Flooring", "LVP flooring"], ["Trim", "Baseboard and casing upgrade"], ["Painting", "Exterior stucco repaint"],
  ["Handyman", "Honey-do list day"]
];

function store(k, v) { try { if (v === undefined) return sessionStorage.getItem(k); sessionStorage.setItem(k, v); } catch (e) { return null; } }

document.addEventListener("DOMContentLoaded", function () {
  // rotating hero word
  var rot = document.getElementById("rot");
  if (rot && !window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
    var words = rot.dataset.words.split("|"), i = 0;
    setInterval(function () {
      i = (i + 1) % words.length; rot.textContent = words[i];
      rot.classList.remove("swap"); void rot.offsetWidth; rot.classList.add("swap");
    }, 2200);
  }

  // real-photo wall painter: keeps the wall's own light and texture, swaps the color
  var cv = document.getElementById("wallcanvas");
  if (cv) {
    var ctx = cv.getContext("2d"), base = new Image(), mask = new Image(), loaded = 0, data = null;
    var ready = function () {
      if (++loaded < 2) return;
      try {
        ctx.drawImage(mask, 0, 0, cv.width, cv.height);
        var m = ctx.getImageData(0, 0, cv.width, cv.height).data;
        ctx.drawImage(base, 0, 0, cv.width, cv.height);
        var px = ctx.getImageData(0, 0, cv.width, cv.height);
        var n = cv.width * cv.height, lum = new Float32Array(n), a = new Float32Array(n), sum = 0, cnt = 0;
        for (var i = 0; i < n; i++) {
          var r = px.data[i * 4], g = px.data[i * 4 + 1], b = px.data[i * 4 + 2];
          lum[i] = (r + g + b) / 3; a[i] = m[i * 4] / 255;
          if (a[i] > 0.9) { sum += lum[i]; cnt++; }
        }
        data = { px: px, orig: new Uint8ClampedArray(px.data), lum: lum, a: a, mean: sum / cnt };
        window.paintWall(document.getElementById("roomwrap").dataset.c);
      } catch (e) { ctx.drawImage(base, 0, 0, cv.width, cv.height); }
    };
    window.paintWall = function (hex) {
      if (!data) return;
      var t = [parseInt(hex.substr(1, 2), 16), parseInt(hex.substr(3, 2), 16), parseInt(hex.substr(5, 2), 16)];
      var d = data.px.data, o = data.orig;
      for (var i = 0; i < data.a.length; i++) {
        var al = data.a[i], k = i * 4;
        if (al === 0) { d[k] = o[k]; d[k + 1] = o[k + 1]; d[k + 2] = o[k + 2]; continue; }
        var f = Math.pow(data.lum[i] / data.mean, 0.8); f = f < 0.5 ? 0.5 : (f > 1.45 ? 1.45 : f);
        for (var c = 0; c < 3; c++) d[k + c] = o[k + c] * (1 - al) + Math.min(255, t[c] * f) * al;
      }
      ctx.putImageData(data.px, 0, 0);
    };
    base.onload = ready; mask.onload = ready;
    base.src = "images/wall-room.jpg"; mask.src = "images/wall-mask.png";
  }

  // Sherwin-Williams color picker
  var rw = document.getElementById("roomwrap");
  if (rw) {
    document.querySelectorAll(".swatch").forEach(function (b) {
      b.addEventListener("click", function () {
        rw.style.setProperty("--wall", b.dataset.c);
        if (window.paintWall) window.paintWall(b.dataset.c);
        document.getElementById("cname").textContent = b.dataset.n;
        document.getElementById("cmeta").textContent = b.dataset.s + " \u00b7 " + b.dataset.y + " Color of the Year";
        document.querySelectorAll(".swatch").forEach(function (x) { x.setAttribute("aria-pressed", x === b ? "true" : "false"); });
      });
    });
  }

  // before/after photo cards
  document.querySelectorAll(".pair").forEach(function (f) {
    f.querySelectorAll(".seg button").forEach(function (b) {
      b.addEventListener("click", function () {
        f.classList.toggle("show-before", b.dataset.v === "before");
        f.querySelectorAll(".seg button").forEach(function (x) { x.setAttribute("aria-pressed", x === b ? "true" : "false"); });
      });
    });
  });

  // before/after slider
  document.querySelectorAll(".compare").forEach(function (c) {
    var r = c.querySelector("input[type=range]");
    var set = function () { c.style.setProperty("--pos", r.value + "%"); };
    r.addEventListener("input", set); set();
  });

  // honey-do list builder
  var hd = document.getElementById("honey-send");
  if (hd) {
    var count = document.getElementById("honey-count");
    var boxes = document.querySelectorAll(".list input[type=checkbox]");
    var upd = function () {
      var n = document.querySelectorAll(".list input:checked").length;
      count.textContent = n + (n === 1 ? " item" : " items");
    };
    boxes.forEach(function (b) { b.addEventListener("change", upd); }); upd();
    hd.addEventListener("click", function () {
      var items = Array.prototype.map.call(document.querySelectorAll(".list input:checked"), function (b) { return b.value; });
      store("h2h-list", items.join("\n"));
    });
  }
  var det = document.getElementById("f-details");
  if (det) {
    var saved = store("h2h-list");
    if (saved) {
      det.value = "My honey-do list:\n- " + saved.split("\n").join("\n- ");
      var hb = document.querySelector("input[value='Handyman list']"); if (hb) hb.checked = true;
    }
  }

  // copy buttons
  document.querySelectorAll(".copy").forEach(function (b) {
    b.addEventListener("click", function () {
      var t = b.getAttribute("data-t");
      var done = function () { b.textContent = "Copied"; setTimeout(function () { b.textContent = "Copy"; }, 1500); };
      try { navigator.clipboard.writeText(t).then(done, function () { selectText(b); }); } catch (e) { selectText(b); }
    });
  });

  // photo gallery
  var gal = document.getElementById("gallery");
  if (gal) {
    var render = function (cat) {
      gal.innerHTML = "";
      if (PHOTOS.length) {
        PHOTOS.filter(function (p) { return cat === "All" || p.cat === cat; }).forEach(function (p) {
          var f = document.createElement("figure"); f.className = "tile";
          var img = document.createElement("img"); img.src = p.src; img.alt = p.caption; img.loading = "lazy";
          var c = document.createElement("figcaption"); c.textContent = p.caption;
          f.appendChild(img);
          if (p.stage) { var t = document.createElement("span"); t.className = "tag"; t.textContent = p.stage; f.appendChild(t); }
          f.appendChild(c); gal.appendChild(f);
        });
      } else {
        PLACEHOLDERS.filter(function (p) { return cat === "All" || p[0] === cat; }).forEach(function (p) {
          var d = document.createElement("div"); d.className = "ph";
          d.innerHTML = "Photo coming soon<br>" + p[1]; gal.appendChild(d);
        });
      }
    };
    document.querySelectorAll(".filters button").forEach(function (b) {
      b.addEventListener("click", function () {
        document.querySelectorAll(".filters button").forEach(function (x) { x.setAttribute("aria-pressed", "false"); });
        b.setAttribute("aria-pressed", "true"); render(b.dataset.cat);
      });
    });
    render("All");
  }

  // reviews
  var rv = document.getElementById("reviews");
  if (rv && REVIEWS.length) {
    document.getElementById("reviews-empty").hidden = true;
    REVIEWS.forEach(function (r) {
      var a = document.createElement("article"); a.className = "rev";
      var s = document.createElement("div"); s.className = "stars"; s.setAttribute("aria-label", r.stars + " out of 5 stars");
      s.textContent = "★★★★★".slice(0, r.stars);
      var p = document.createElement("p"); p.textContent = "“" + r.text + "”";
      var w = document.createElement("p"); w.className = "muted"; w.textContent = r.name + " · " + r.city + (r.source ? " · via " + r.source : "");
      a.appendChild(s); a.appendChild(p); a.appendChild(w); rv.appendChild(a);
    });
  }

  // estimate form: inside a preview frame there is nowhere to send it
  var form = document.querySelector("form[name='estimate']");
  if (form && window.top !== window.self) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var n = document.getElementById("preview-note"); if (n) n.hidden = false;
    });
  }
});

function selectText(b) {
  var v = b.parentNode.querySelector(".v"); if (!v) return;
  var r = document.createRange(); r.selectNodeContents(v);
  var s = window.getSelection(); s.removeAllRanges(); s.addRange(r);
}
