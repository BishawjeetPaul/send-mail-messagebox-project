/*----------------------------------------
# SCRIPTS HERE IT WILL EXTEND TO HOME PAGE
----------------------------------------*/

// 1) Character remaining counter
$(document).ready(function() {
    var start = 0;
    var limit = 1000;

    $("#message").keyup(function() {
        start = this.value.length;
        if (start > limit) {
            return false;
        }
        else if (start == 1000) {
            $("#remaining").html("Character remaining: " + (limit - start)).css('color', 'red');
            swal("Opps !", "Characters limit exceeded !", "info");
        }
        else if (start > 984) {
            $("#remaining").html("Character remaining: " + (limit - start)).css('color', 'red');
            swal("Opps !", "Characters limit exceeded !", "info");
        }
        else if (start < 1000) {
            $("#remaining").html("Character remaining: " + (limit - start)).css('color', 'black');  
        }
        else {
            $("#remaining").html("Character remaining: " + (limit)).css('color', 'black');
        }
    });
});


// 2) Inputmask (PHONE)
$(document).ready(function() {
    $('.phone').inputmask("(999) 999-9999", {"onincomplete": function() {
        swal("Opps !", "Incomplete phone. Please review !", "info");
        $(".phone").val("");
        return false;
    }});
});