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
//open modal window
/* $(document).ready(
  $(function () {
    //call button click
    $(".call-button").click(function () {
      $("modal-phone-call-container").css("display", "block");
    });
  })
); */
//close modal window
/* $(document).ready(
	$(function () {
	  //call button click
	  $(".modal-phone-call-close").click(function () {
		$("modal-phone-call-container").css("display", "none");
	  });
	})
  ); */
//
/* $(function () {
	var buttoncall = $("call-button");
	buttoncall.click(function () {
		$(".modal-phone-call-container").css("display","block");	
	});
}); */
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