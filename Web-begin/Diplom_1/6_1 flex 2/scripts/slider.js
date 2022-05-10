$(document).ready(function() {

	new Swiper(".swiper", {
    	slidesPerView: 3,
		lazy: true,
		spaceBetween: 20,
		loop: true,
		pagination: {
			el:".swiper-pagination",
			clickable:true,
		},
		navigation: {
          nextEl: ".what-i-do-examples-arrow-right",
          prevEl: ".what-i-do-examples-arrow-left",
        },
		breakpoints: {
			320: {
				slidesPerView: 1,
				spaceBetween: 10,
			},
			1024: {
				slidesPerView: 2,
				spaceBetween: 10,
			},
			1200: {
				slidesPerView: 3,
				spaceBetween: 20,
				pagination: false
			}
		}
      });
});