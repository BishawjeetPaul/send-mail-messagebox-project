// 1) Script to get the Time running at realtime
setInterval(function() {
    var date = new Date();
    $('#clock').html(
        (date.getHours() < 10 ? '0' : '') + date.getHours() + ":" +
        (date.getMinutes() < 10 ? '0' : '') + date.getMinutes() + ":" +
        (date.getSeconds() < 10 ? '0' : '') + date.getSeconds()
    );
}, 500);


// 2) Script to update the page always at (0:00)
function autoRefresh(hours, minutes, seconds) {
    var now = new Date();
    var then = new Date();
    
    then.setHours(hours, minutes, seconds, 0);
    if(then.getTime() < now.getTime()) {
        then.getDate(now.getDate() + 1);
    }
    var timeout = (then.getTime() - now.getTime());
    setTimeout(function() {
        window.location.reload(True);
    }, timeout);
};
autoRefresh(0,0,0);

// 3) If no messages, hide all content
$(document).ready(function() {
    var verify = $('#chk_td').length;
        if (verify == 0) {
            $(".hide").css('display', 'none');
            $("#msg").text("No message found");
            $('#refresh').html('<i class="fas fa-sync-alt fa-3x">');
        }
});