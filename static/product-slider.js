const productSlides = document.querySelector('.product-slides');
    const totalProducts = productSlides.children.length;
    let productsPerView = 4; // Default: 4 products visible
    let currentIndex = 0;

    // Function to update productsPerView based on screen size
    function updateProductsPerView() {
      const width = window.innerWidth;
      if (width <= 768) {
        productsPerView = 1; // 1 product visible on mobile
      } else if (width <= 1024) {
        productsPerView = 3; // 3 products visible on tablet
      } else {
        productsPerView = 4; // 4 products visible on desktop
      }
    }

    // Function to slide to the next product
    function nextSlide() {
      const maxIndex = totalProducts - productsPerView;
      currentIndex++;
      if (currentIndex > maxIndex) {
        currentIndex = 0; // Loop back to the first slide
      }
      updateProductSlide();
    }

    // Function to slide to the previous product
    function prevSlide() {
      currentIndex--;
      if (currentIndex < 0) {
        currentIndex = totalProducts - productsPerView; // Go to the last group of slides
      }
      updateProductSlide();
    }

    // Update the sliding position
    function updateProductSlide() {
      const offset = -currentIndex * (100 / productsPerView);
      productSlides.style.transform = `translateX(${offset}%)`;
    }

    // Auto-slide functionality
    function autoSlideProducts() {
      nextSlide();
    }

    // Set interval to slide automatically every 2 seconds
    let autoSlideInterval = setInterval(autoSlideProducts, 3000);

    // Pause auto sliding when buttons are clicked
    function pauseAutoSlide() {
      clearInterval(autoSlideInterval);
      autoSlideInterval = setInterval(autoSlideProducts, 3000); // Resume auto sliding after a short delay
    }

    // Event listeners for buttons
    document.getElementById('next').addEventListener('click', () => {
      nextSlide();
      pauseAutoSlide();
    });

    document.getElementById('prev').addEventListener('click', () => {
      prevSlide();
      pauseAutoSlide();
    });

    // Initial call to set products per view
    updateProductsPerView();

    // Update productsPerView and slide position on window resize
    window.addEventListener('resize', () => {
      updateProductsPerView();
      updateProductSlide();
    });