/* ======= Preloader ======= */

/* ======= Testinomial Slider ======= */
 $('.slider-for').slick({
  slidesToShow: 1,
  slidesToScroll: 1,
  arrows: false,
  fade: true,
  asNavFor: '.slider-nav'
});

$('.slider-nav').slick({
  slidesToShow: 5,
  slidesToScroll: 1,
  asNavFor: '.slider-for',
  dots: false,
  centerMode: true,
  focusOnSelect: true,
  responsive: [
    {
      breakpoint: 991,
      settings: {
        slidesToShow: 3,
        slidesToScroll: 1,
      }
    }, 
  ]
}).on('beforeChange', function(event, slick, currentSlide, nextSlide){
  RemoveClass();
  AddClass();
});

$(".slick-prev").click(function(){
	RemoveClass();
	AddClass();
});

$(".slick-next").click(function(){
	RemoveClass();
	AddClass();
});

// On edge hit
$('.slider-nav').on('edge', function(event, slick, direction){
  	RemoveClass();
	AddClass();
});

// On swipe event	
$('.slider-nav').on('swipe', function(event, slick, direction){
	RemoveClass();
	AddClass();
});

$('.slider-nav').click(function(e) {
  RemoveClass();
	AddClass();
});


$( document ).ready(function() {	
	AddClass();
});

function RemoveClass() {
	$('div.slick-slide').removeClass('first');
	$('div.slick-slide').removeClass('second');
	$('div.slick-slide').removeClass('third');
	$('div.slick-slide').removeClass('fourth');
	$('div.slick-slide').removeClass('fifth');
	$('div.slick-slide').removeClass('sixth');
	$('div.slick-slide').removeClass('seven');
}

function AddClass() {
	$('.slick-track').find('.slick-center').addClass('third');
	$('.slick-center').prev("div.slick-active:first").addClass("first");
	$('.slick-center').prev("div.slick-active:first").prev("div.slick-active").addClass("second");
	$('.second').prev("div.slick-slide").addClass("sixth");
	$('.slick-center').next("div.slick-active:first").addClass("fourth");
	$('.slick-center').next("div.slick-active:first").next("div.slick-active").addClass("fifth");
	$('.fifth').next("div.slick-slide").addClass("seven");
}
$(document).ready(function($) {
	$(window).on('load',function(){
		$('#preloader').fadeOut('slow',function(){$(this).remove();});
	});
	/* ======= Scrolllt ======= */
	$.scrollIt({
		topOffset: -95, // offste (in px) for fixed top navigation        
	});

	/* ======= Accordian ======= */
	function toggleIcon(e) {
		$(e.target)
			.prev('.panel-heading')
			.find(".more-less")
			.toggleClass('glyphicon-plus glyphicon-minus');
	}
	$('.panel-group').on('hidden.bs.collapse', toggleIcon);
	$('.panel-group').on('shown.bs.collapse', toggleIcon);
	
	/* ======= Isotop-Portfolio-Filer  ======= */
	$(window).load(function() {
		  "use strict";
		var $container = $('.portfolio-gal');
		$container.isotope({
			itemSelector : '.portfolio-gal .col-xs-12.col-sm-4',
			transitionDuration: '0.6s'
		});
		var $optionSets = $('.portfolio-gal-filter'),
			$optionLinks = $optionSets.find('a');
		$optionLinks.click(function(){
			var $this = $(this);
			// don't proceed if already selected
			if ( $this.hasClass('active') ) {
				return false;
			}
			var $optionSet = $this.parents('.portfolio-gal-filter');
			$optionSet.find('.active').removeClass('active');
			$this.addClass('active');
		// make option object dynamically, i.e. { filter: '.my-filter-class' }
		var options = {},
			key = $optionSet.attr('data-option-key'),
			value = $this.attr('data-option-value');
			
		// parse 'false' as false boolean
		value = value === 'false' ? false : value;
		options[ key ] = value;
			if ( key === 'layoutMode' && typeof changeLayoutMode === 'function' ) {
			changeLayoutMode( $this, options );
		} else {
			// otherwise, apply new options
			$container.isotope( options );
		}    
		return false;
		});
	});
	
	//animatation 
	wow = new WOW(
      {
        animateClass: 'animated',
        offset:       100,
        callback:     function(box) {
          console.log("WOW: animating <" + box.tagName.toLowerCase() + ">")
        }
      }
    );
    wow.init();
    document.getElementById('moar').onclick = function() {
      var section = document.createElement('section');
      section.className = 'section--purple wow fadeInDown';
      this.parentNode.insertBefore(section, this);
    };
});

// FancyBox
	$(".fancybox").fancybox({
		openEffect	: 'none',
		closeEffect	: 'none'
	});