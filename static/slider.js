 const slides = document.querySelector('.carousel-slides');
    const totalSlides = slides.children.length;
    let currentSlide = 0;

    // Function to update the slide position
    function updateSlide() {
      const offset = -currentSlide * 100;
      slides.style.transform = `translateX(${offset}%)`;
    }

    // Auto-slide every 3 seconds
    function autoSlide() {
      currentSlide = (currentSlide + 1) % totalSlides;
      updateSlide();
    }

    // Set interval for automatic sliding
    let slideInterval = setInterval(autoSlide, 3000);

    // Next and previous button functionality
    document.getElementById('next-slide').addEventListener('click', () => {
      clearInterval(slideInterval); // Reset the interval when clicked
      currentSlide = (currentSlide + 1) % totalSlides;
      updateSlide();
      slideInterval = setInterval(autoSlide, 3000); // Restart the interval
    });

    document.getElementById('preview').addEventListener('click', () => {
      clearInterval(slideInterval); // Reset the interval when clicked
      currentSlide = (currentSlide - 1 + totalSlides) % totalSlides;
      updateSlide();
      slideInterval = setInterval(autoSlide, 3000); // Restart the interval
    });