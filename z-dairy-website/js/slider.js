let slides = document.querySelectorAll(".slide");
let i = 0;

setInterval(() => {
  slides.forEach(slide => slide.classList.remove("active"));
  slides[i].classList.add("active");
  i = (i + 1) % slides.length;
}, 4000);

// ============== fun-2

  const modal = document.getElementById("viewModal");
  const modalImg = document.getElementById("modalImg");
  const modalTitle = document.getElementById("modalTitle");
  const closeBtn = document.querySelector(".close");

  document.addEventListener("click", e => {
    const btn = e.target.closest(".action-button");
    if (!btn) return;

    const card = btn.closest(".card");
    modalImg.src = card.querySelector("img").src;
    modalTitle.innerText = card.querySelector("h3").innerText;

    modal.style.display = "flex";
  });

  closeBtn.onclick = () => modal.style.display = "none";

