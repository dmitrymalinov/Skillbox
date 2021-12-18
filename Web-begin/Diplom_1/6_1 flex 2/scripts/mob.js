$(function () {
  $(".mobile-menu").click(function () {
    var menu = $(".nav-class");
    menu.slideToggle(500);
  });
});
$(document).ready(
  $(function () {
    //phone mask
    $(".phone-class").mask("8(999) 999-99-99");
  })
);
//call button
$(document).ready(
	$(function () {
		var buttoncall = $(".call-button");
		buttoncall.click(function () {
			$(".modal-phone-call-container").css("display","block");	
		});
		
	})	
);
$(document).ready(
	$(function () {
		var buttoncall = $(".modal-phone-call-close");
		buttoncall.click(function () {
			$(".modal-phone-call-container").css("display","none");	
		});
	})	
);
$(document).ready(
	$(function () {
		var buttonsendcall = $(".modal-phone-call-content-send-button");
		buttonsendcall.click(function () {
			$(".modal-phone-call-container").css("display","none");	
		});
	})	
);
// price what-i-do-price
$(document).ready(
	$(function () {
		var buttoncall = $(".what-i-do-price");
		buttoncall.click(function () {
			$(".modal-what-i-do-price-container").css("display","block");	
		});
	})	
);
$(document).ready(
	$(function () {
		var buttoncall = $(".modal-what-i-do-price-close");
		buttoncall.click(function () {
			$(".modal-what-i-do-price-container").css("display","none");	
		});
	})	
);
$(document).ready(
	$(function () {
		var buttonsendcall = $(".modal-what-i-do-price-content-send-button");
		buttonsendcall.click(function () {
			$(".modal-what-i-do-price-container").css("display","none");	
		});
	})	
);
//know-more
$(document).ready(
	$(function () {
		var buttonKnowMore = $(".know-more");
		buttonKnowMore.click(function () {
			$(".know-more-modal-container").css("display","block");	
		});
	})	
);
$(document).ready(
	$(function () {
		var buttonKnowMoreclose = $(".modal-know-more-close");
		buttonKnowMoreclose.click(function () {
			$(".know-more-modal-container").css("display","none");	
		});
	})	
);
$(document).ready(
	$(function () {
		var buttonsendcallKnowMoreSend = $(".modal-know-more-content-send-button");
		buttonsendcallKnowMoreSend.click(function () {
			$(".know-more-modal-container").css("display","none");	
		});
	})	
);