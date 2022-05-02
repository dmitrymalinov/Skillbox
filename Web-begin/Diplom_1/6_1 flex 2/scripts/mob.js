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
//phone-call button for 360px button
$(document).ready(
	$(function () {
		var buttoncall = $(".phone-call");
		buttoncall.click(function () {
			$(".modal-phone-call-container").css("display","block");	
		});
		
	})	
);
//
$(document).ready(
	$(function () {
		var buttoncall = $(".modal-phone-call-close");
		buttoncall.click(function () {
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
//validations
function ValidateMenu() {
	errorFieldClass = 'justvalidate-invalid';
	errorLabelCssClass = 'justvalidate-invalid-label';
	rules = {
		rule1:{
			field:"#modal-phone-call-input-text",
			rule: "required",
            errorMessage: "Укажите Ваше имя",
		},
		rule2:{
			field:"#phone-class-input",
			rule: "required",
            errorMessage: "Укажите телефон",
		}
	};
	classToHide = ".modal-phone-call-container";
	selector = '#modal-phone-call-container';
	ValidateTopMod({selector,rules,errorFieldClass,errorLabelCssClass,classToHide})
}
function KnowMoreValidate() {
	errorFieldClass = 'justvalidate-invalid';
	errorLabelCssClass = 'justvalidate-invalid-label';
	rules = {
		rule1:{
			field:"#modal-know-more-input-text",
			rule: "required",
            errorMessage: "Укажите Ваше имя",
		},
		rule2:{
			field:"#phone-class-input-knowmore",
			rule: "required",
            errorMessage: "Укажите телефон",
		},
		rule3:{
			field:"#modal-know-more-input-text-email",
			rule: "required",
            errorMessage: "Укажите e-mail",
		}
	};
	classToHide = ".know-more-modal-container";
	selector = '#know-more-modal-container';
	ValidateTopMod({selector,rules,errorFieldClass,errorLabelCssClass,classToHide})
}
function KnowPriceValidate() {
	errorFieldClass = 'justvalidate-invalid';
	errorLabelCssClass = 'justvalidate-invalid-label';
	rules = {
		rule1:{
			field:"#modal-what-i-do-price-input-text",
			rule: "required",
            errorMessage: "Укажите Ваше имя",
		},
		rule2:{
			field:"#phone-class-input-price",
			rule: "required",
            errorMessage: "Укажите телефон",
		},
		rule3:{
			field:"#modal-what-i-do-price-input-text-email",
			rule: "required",
            errorMessage: "Укажите e-mail",
		}
	};
	classToHide = ".modal-what-i-do-price-container";
	selector = '#modal-what-i-do-price-container';
	ValidateTopMod({selector,rules,errorFieldClass,errorLabelCssClass,classToHide})
}
function ValidateTopMod({selector,rules,ErrorFieldClass,errorLabelCssClass,classToHide}) {
	const validation = new window.JustValidate(selector,{
		errorFieldCssClass: ErrorFieldClass,
		focusInvalidField: true,
		errorLabelCssClass: errorLabelCssClass,
    	//lockForm: true,
	},);
	for (const key in rules) {//ruleElement
		if (Object.hasOwnProperty.call(rules, key)) {
			const singleruleelement = rules[key];
			validation.addField(singleruleelement.field,[{rule:rules[key].rule,errorMessage:rules[key].errorMessage}])
		}
	}
	validation.onSuccess((event) => {
		$(classToHide).css("display","none");
	  });
}



