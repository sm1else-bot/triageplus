"use strict";
const viewer = document.querySelector("#viewer");
const image = document.querySelector("#viewer-image");
const caption = document.querySelector("#viewer-caption");
let opener;
for (const link of document.querySelectorAll("[data-image]")) {
  link.addEventListener("click", (event) => {
    // Preserve modified-click navigation and a useful no-JavaScript fallback.
    if (event.metaKey || event.ctrlKey || event.shiftKey || event.altKey)
      return;
    event.preventDefault();
    opener = link;
    const thumbnail = link.querySelector("img");
    image.src = link.href;
    image.alt = thumbnail.alt;
    caption.textContent = link
      .closest("figure")
      .querySelector("figcaption").innerText;
    document.querySelector("#original-link").href = link.href;
    viewer.showModal();
    document.querySelector("#viewer-close").focus();
  });
}
document
  .querySelector("#viewer-close")
  .addEventListener("click", () => viewer.close());
viewer.addEventListener("click", (event) => {
  if (event.target === viewer) {
    const r = viewer.getBoundingClientRect();
    if (
      event.clientX < r.left ||
      event.clientX > r.right ||
      event.clientY < r.top ||
      event.clientY > r.bottom
    )
      viewer.close();
  }
});
viewer.addEventListener("close", () => {
  image.removeAttribute("src");
  opener?.focus();
});
const links = [...document.querySelectorAll(".contents a")];
const sections = links.map((link) => document.querySelector(link.hash));
if ("IntersectionObserver" in window) {
  const visible = new Set();
  const observer = new IntersectionObserver(
    (entries) => {
      for (const entry of entries)
        entry.isIntersecting
          ? visible.add(entry.target)
          : visible.delete(entry.target);
      const active = sections.find((section) => visible.has(section));
      if (active)
        for (const link of links)
          link.setAttribute(
            "aria-current",
            String(link.hash === "#" + active.id),
          );
    },
    { rootMargin: "-5% 0px -55% 0px", threshold: 0 },
  );
  sections.forEach((section) => observer.observe(section));
}
