// Simple, dependency-free slider that supports two markup styles
(function () {
  const sliders = document.querySelectorAll('.slider');
  if (!sliders.length) return;

  sliders.forEach(initSlider);

  function initSlider(slider) {
    const slidesWrap = slider.querySelector('.slides');
    const slides = slidesWrap ? slidesWrap.querySelectorAll('.slide') : slider.querySelectorAll('.slide');
    const prev = slider.querySelector('.prev');
    const next = slider.querySelector('.next');
    const dotsContainer = slider.querySelector('.dots');
    const interval = parseInt(slider.dataset.interval, 10) || 4000;

    let index = 0;
    let timer = null;

    function update() {
      if (slidesWrap) {
        slidesWrap.style.transform = `translateX(-${index * 100}%)`;
      } else {
        slides.forEach((s, i) => s.classList.toggle('active', i === index));
      }
      updateDots();
    }

    function prevSlide() {
      index = (index - 1 + slides.length) % slides.length;
      update();
    }

    function nextSlide() {
      index = (index + 1) % slides.length;
      update();
    }

    function goTo(i) {
      index = (i + slides.length) % slides.length;
      update();
    }

    function start() {
      stop();
      timer = setInterval(nextSlide, interval);
    }

    function stop() {
      if (timer) {
        clearInterval(timer);
        timer = null;
      }
    }

    function createDots() {
      if (!dotsContainer) return;
      dotsContainer.innerHTML = '';
      slides.forEach((_, i) => {
        const btn = document.createElement('button');
        btn.className = 'dot';
        btn.setAttribute('aria-label', `Go to slide ${i + 1}`);
        btn.addEventListener('click', () => goTo(i));
        dotsContainer.appendChild(btn);
      });
    }

    function updateDots() {
      if (!dotsContainer) return;
      const dots = dotsContainer.querySelectorAll('.dot');
      dots.forEach((d, i) => d.classList.toggle('active', i === index));
    }

    if (prev) prev.addEventListener('click', prevSlide);
    if (next) next.addEventListener('click', nextSlide);

    if (dotsContainer) createDots();

    slider.addEventListener('mouseenter', stop);
    slider.addEventListener('mouseleave', start);

    if (slidesWrap) {
      slidesWrap.style.display = 'flex';
      slidesWrap.style.transition = 'transform 0.45s ease';
      slides.forEach(slide => slide.style.minWidth = '100%');
    } else {
      slides.forEach((s, i) => s.classList.toggle('active', i === 0));
    }

    update();
    start();
  }
})();
