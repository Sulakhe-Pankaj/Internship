let slides = document.querySelectorAll(".slide");
let i = 0;

setInterval(() => {
  slides.forEach(slide => slide.classList.remove("active"));
  slides[i].classList.add("active");
  i = (i + 1) % slides.length;
}, 4000);
