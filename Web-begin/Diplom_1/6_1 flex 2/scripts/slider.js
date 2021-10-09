$(document).ready(function() {

	var swiper = new Swiper(".mySwiper", {
    	slidesPerView: 3,
		lazy: true,
		spaceBetween: 20,
		loop: true,
		navigation: {
          nextEl: ".what-i-do-examples-arrow-right",
          prevEl: ".what-i-do-examples-arrow-left",
        },
		breakpoints: {
			320: {
				slidesPerView: 1,
				spaceBetween: 10,
				pagination: {
					el:".swiper-pagination",
				}
			},
			1024: {
				slidesPerView: 2,
				spaceBetween: 10,
				pagination: {
					el:".swiper-pagination",
				}
			},
			1920: {
				slidesPerView: 3,
				spaceBetween: 20,
			}
		}
      });
});