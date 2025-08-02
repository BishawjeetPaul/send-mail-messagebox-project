/* -- Ajax Back Spinner -- */
$(document).ready(function() {
    console.log("hello.....");
    jQuery(function($) {
        $(document).ajaxSend(function() {
            $("#bg-spinner").fadeIn(300);
        });
    
        $(".send-email").click(function() {
            $.ajax({
                type: 'GET',
                success:function(data) {
                    // console.log(data);
                    var d = $.parseJSON(data);
                    alert(d.Test);
                }
            }).done(function() {
                setTimeout(function() {
                    $("#bg-spinner").fadeOut(300);
                }, 1000);
            });
        });
    });
    // Close modal (after 'send button is clicked')
    $(".send-email").click(function() {
        var msg = $("#email-msg").val();
        var subject = $("#email-subject").val();

        if ((msg != '')  && (subject != '')) {
            $('.close-modal').modal('hide');
        }
    });
});


// Script to advice the users about logout at 5 min (after 25min)
setTimeout(function() {
    var notice = document.querySelector("#warning");
    if (notice) {
        notice.click();
    }
}, 1 * 10000); // 25 min


// Script to auto logout(after 5 minutes passed)
setTimeout(function() {
    var notice = document.querySelector("#warning");
    if (notice) {
        notice.click();
    }
}, 1 * 15000); // 30 min