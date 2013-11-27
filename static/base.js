$(document).ready(function() {
    function get_timestamp() {
        var date = new Date();        
        var time = date.getHours() + ":";
        time += ((date.getMinutes() < 10) ? "0" : "") + date.getMinutes() + ":";
        time += ((date.getSeconds() < 10) ? "0" : "") + date.getSeconds();
        time = "< " + time + ">: ";
        return time;
    }

    function handle_send() {

    }

    $("#send_message_button").click(function() {
        handle_send();
    })
    $("#chat_message").bind('keypress', function(e) {
        var code = e.keyCode || e.which;
        if (code == 13) { //Enter keycode
            handle_send();
        }
    });
});