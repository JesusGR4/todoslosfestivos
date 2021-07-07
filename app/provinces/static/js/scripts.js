/*!
    * Start Bootstrap - Grayscale v6.0.3 (https://startbootstrap.com/theme/grayscale)
    * Copyright 2013-2020 Start Bootstrap
    * Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-grayscale/blob/master/LICENSE)
    */
(function ($) {
    "use strict"; // Start of use strict

    // Smooth scrolling using jQuery easing
    $('a.js-scroll-trigger[href*="#"]:not([href="#"])').click(function () {
        if (
            location.pathname.replace(/^\//, "") ==
            this.pathname.replace(/^\//, "") &&
            location.hostname == this.hostname
        ) {
            var target = $(this.hash);
            target = target.length
                ? target
                : $("[name=" + this.hash.slice(1) + "]");
            if (target.length) {
                $("html, body").animate(
                    {
                        scrollTop: target.offset().top - 70,
                    },
                    1000,
                    "easeInOutExpo"
                );
                return false;
            }
        }
    });

    // Closes responsive menu when a scroll trigger link is clicked
    $(".js-scroll-trigger").click(function () {
        $(".navbar-collapse").collapse("hide");
    });

    // Activate scrollspy to add active class to navbar items on scroll
    $("body").scrollspy({
        target: "#mainNav",
        offset: 100,
    });

    // Collapse Navbar
    var navbarCollapse = function () {
        if ($("#mainNav").length > 0) {
            if ($("#mainNav").offset().top > 100) {
                $("#mainNav").addClass("navbar-shrink");
            } else {
                $("#mainNav").removeClass("navbar-shrink");
            }
        }
    };
    // Collapse now if page is not at top
    navbarCollapse();
    // Collapse the navbar when page is scrolled
    $(window).scroll(navbarCollapse);
})(jQuery); // End of use strict

$('#language-list a').on('click', function (event) {
    event.preventDefault();
    var target = $(event.target);
    var url = target.attr('href');
    var language_code = target.data('language-code');
    $.ajax({
        type: 'POST',
        url: url,
        data: {language: language_code},
        headers: {"X-CSRFToken": $('#csrf_token').val()}
    }).done(function (data, textStatus, jqXHR) {
        reload_page();
    });
});
$('#punxes').on('click', function (event) {
    $('#punxes-modal').modal('toggle')
})

$('#sant-pau').on('click', function (event) {
    $('#sant-pau-modal').modal('toggle')
})
$('#write-solution-1').on('click', function (event) {
    $('#modal-solution-1').modal('toggle')
})
$('#write-solution-2').on('click', function (event) {
    $('#modal-solution-2').modal('toggle')
})
$('#write-solution-3').on('click', function (event) {
    $('#modal-solution-3').modal('toggle')
})

$('#write-solution-4').on('click', function (event) {
    $('#modal-solution-4').modal('toggle')
})

$('#pista-2').on('click', function (event) {
    $('#modal-pista-2').modal('toggle')
})
$('#pista-3').on('click', function (event) {
    $('#modal-pista-3').modal('toggle')
})

$('#pista-4').on('click', function (event) {
    $('#modal-pista-4').modal('toggle')
})

$('#check-3').on('click', function (event) {
    var solution = $('#solution-3').val()
    var $errors = $('#errors-3')
    $errors.hide()
    if (solution.toUpperCase() == "SAGRADA FAMILIA") {
        window.location.href = "https://xperifun.com/p/segundo-plato/";
    } else {
        $errors.show()
    }
})

$('#check-1').on('click', function (event) {
    var solution = $('#solution-1').val()
    var $errors = $('#errors-1')
    $errors.hide()
    if (solution.toUpperCase() == "REUS") {
        window.location.href = "https://xperifun.com/p/cata/";
    } else {
        $errors.show()
    }
})

$('#check-4').on('click', function (event) {
    var solution = $('#solution-4').val()
    var $errors = $('#errors-4')
    $errors.hide()
    if (solution == "33") {
        window.location.href = "https://xperifun.com/p/postres/";
    } else {
        $errors.show()
    }
})
$('#check-2').on('click', function (event) {
    var solution = $('#solution-2').val()
    var $errors = $('#errors-2')
    $errors.hide()
    if (solution.toUpperCase() == "VICENS") {
        window.location.href = "https://xperifun.com/p/primer-plato/";
    } else {
        $errors.show()
    }
})
$('#help-1').on('click', function (event) {
    $('#modal-help-1').modal('toggle')
})
$('#help-4').on('click', function (event) {
    $('#modal-help-4').modal('toggle')
})

$('#help-2').on('click', function (event) {
    $('#modal-help-2').modal('toggle')
})
$('#help-3').on('click', function (event) {
    $('#modal-help-3').modal('toggle')
})
$('#bellesguard').on('click', function () {
    window.location.href = "https://xperifun.com/p/enhorabuena-bellesguard/";
})

function getCookie(name) {
    var value = '; ' + document.cookie,
        parts = value.split('; ' + name + '=');
    if (parts.length == 2) return parts.pop().split(';').shift();
}

function reload_page() {
    window.location.reload(true);
}

/**********************Scroll Animation "START"************************************/
$(document).ready(function () {
    var $animation_elements = $('.anim');
    var $window = $(window);

    function check_if_in_view() {
        var window_height = $window.height();
        var window_top_position = $window.scrollTop();
        var window_bottom_position = (window_top_position + window_height);

        $.each($animation_elements, function () {
            var $element = $(this);
            var element_height = $element.outerHeight();
            var element_top_position = $element.offset().top;
            var element_bottom_position = (element_top_position + element_height);

//check to see if this current container is within viewport
            if ((element_bottom_position >= window_top_position) &&
                (element_top_position <= window_bottom_position)) {
                $element.addClass('animated');
            } else {
                $element.removeClass('animated');
            }
        });
    }

    $window.on('scroll resize', check_if_in_view);
    $window.trigger('scroll');
});
/**********************Scroll Animation "END"************************************/

/**********************Change color of center aligned animated content small Circle  "START"************************************/
$(document).ready(function () {
    $(" .debits").hover(function () {
        $(" .center-right").css("background-color", "#4997cd");
    }, function () {
        $(" .center-right").css("background-color", "#fff");
    });
});
$(document).ready(function () {
    $(".credits").hover(function () {
        $(".center-left").css("background-color", "#4997cd");
    }, function () {
        $(".center-left").css("background-color", "#fff");
    });
});
/**********************Change color of center aligned animated content small Circle  "END"************************************/
function simulate_a(url){
    window.open(url, '_blank');
}
