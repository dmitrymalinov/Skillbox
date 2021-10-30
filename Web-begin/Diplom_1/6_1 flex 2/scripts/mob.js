$(function(){
	$('.mobile-menu').click(function(){
		var menu = $('.nav-class');
		menu.slideToggle(500);
  	})
});
$(document).ready(
	function () {
  console.log("document loaded");
  $(function () {
    //2. Получить элемент, к которому необходимо добавить маску
    $(".phone-class").mask("8(999) 999-99-99");
  });
  // modal window for phone call
  //open window
$(function(){
	//modal conntainer
	//var ModalPhoneCallContainer = $('modal-phone-call-container');
	//var CallButton = $('call-button');
	//var ModalPhoneCallClose = $('modal-phone-call-close');
	//events
	$('call-button').click(function () {
		$('modal-phone-call-container').css('display','block');	
	})
		

});