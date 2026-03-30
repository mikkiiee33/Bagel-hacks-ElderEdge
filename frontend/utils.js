const API = "http://127.0.0.1:5000";

async function apiFetch(path, options = {}) {
  try {
    const res = await fetch(API + path, {
      headers: { "Content-Type": "application/json" },
      ...options,
    });
    if (!res.ok) throw new Error(await res.text());
    return await res.json();
  } catch (e) {
    console.error("API error:", e);
    throw e;
  }
}

function showToast(msg, type = "success") {
  let t = document.getElementById("toast");
  if (!t) {
    t = document.createElement("div");
    t.id = "toast";
    t.className = "toast";
    document.body.appendChild(t);
  }
  const icon = type === "success" ? "✓" : "✕";
  const color = type === "success" ? "var(--green)" : "var(--red)";
  t.innerHTML = `<span style="color:${color};font-weight:700">${icon}</span> ${msg}`;
  t.className = `toast ${type} show`;
  setTimeout(() => t.classList.remove("show"), 3500);
}

function getParam(key) {
  return new URLSearchParams(window.location.search).get(key);
}

function renderStars(n, max = 5) {
  const filled = Math.round(n || 0);
  return Array.from({ length: max }, (_, i) =>
    `<span style="color:${i < filled ? "var(--accent)" : "var(--text-dim)"}">★</span>`
  ).join("");
}

function initials(name) {
  return name.split(" ").slice(0, 2).map(w => w[0]).join("").toUpperCase();
}

function avatar(mentor) {
  if (mentor.photo_url) {
    return `<img class="mentor-avatar" src="${mentor.photo_url}" alt="${mentor.name}" onerror="this.replaceWith(avatarPlaceholder('${initials(mentor.name)}'))">`;
  }
  return `<div class="mentor-avatar-placeholder">${initials(mentor.name)}</div>`;
}

function avatarPlaceholder(letters) {
  const el = document.createElement("div");
  el.className = "mentor-avatar-placeholder";
  el.textContent = letters;
  return el;
}

function currencySymbol(currency) {
  const map = { USD: "$", GBP: "£", EUR: "€", INR: "₹", CAD: "CA$", AUD: "A$", NGN: "₦", MXN: "MX$" };
  return map[currency] || "$";
}

function formatPrice(mentor) {
  const sym = currencySymbol(mentor.currency || "USD");
  const price = mentor.price_usd || mentor.price || "0";
  return `${sym}${price}<span>/session</span>`;
}

function skeletonCards(n = 6) {
  return Array.from({ length: n }, () => `
    <div class="card" style="padding:1.5rem">
      <div style="display:flex;gap:1rem;align-items:flex-start;margin-bottom:1rem">
        <div class="skeleton" style="width:56px;height:56px;border-radius:50%;flex-shrink:0"></div>
        <div style="flex:1">
          <div class="skeleton" style="height:16px;width:70%;margin-bottom:8px"></div>
          <div class="skeleton" style="height:12px;width:90%"></div>
        </div>
      </div>
      <div class="skeleton" style="height:12px;width:100%;margin-bottom:6px"></div>
      <div class="skeleton" style="height:12px;width:80%"></div>
    </div>
  `).join("");
}

function setActive(linkId) {
  document.querySelectorAll(".nav-links a").forEach(a => a.classList.remove("active"));
  const el = document.getElementById(linkId);
  if (el) el.classList.add("active");
}