let currentIndex = 0;
        const slides = document.querySelectorAll('.slide');
        const slider = document.getElementById('slider');
        const slideWidth = slides[0].offsetWidth;

        function nextSlide() {
            if (currentIndex < slides.length - 1) {
                currentIndex++;
            } else {
                currentIndex = 0;
            }
            updateSlider();
        }

        function prevSlide() {
            if (currentIndex > 0) {
                currentIndex--;
            } else {
                currentIndex = slides.length - 1;
            }
            updateSlider();
        }

        function updateSlider() {
            const offset = -currentIndex * slideWidth;
            slider.style.transform = `translateX(${offset}px)`;
        }

        setInterval(nextSlide, 5000);