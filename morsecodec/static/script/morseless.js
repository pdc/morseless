var Morseless = (function($) {
    var ajaxUrl;
    var out;
    var timeoutID;

    function update() {
        //window.log.debug('update');
        if (timeoutID) {
            clearTimeout(timeoutID);
            timeoutID = null;
        }
        var morse = $('#morse').val();
        $.getJSON(ajaxUrl, {morse: morse}, function (data, textStatus, jqXHR) {
            out.val(data.text);
        });
    }
    function scheduleUpdate() {
        //window.log.debug('scheduleUpdate');
        if (!timeoutID) {
            timeoutID = setTimeout(function () {
                timeoutID = null;
                update();
            }, 750);
        }
    }

    return {
        init: function (url) {
            ajaxUrl = url;

            // Change the UI to use AJAX.
            $('form .buttons').remove();
            $('form').submit(function () {
                return false; // Prevent form submission
            })
            var div = $('<div>').appendTo('form');
            $('<label>').text('Text').appendTo(div);
            out = $('<input type="text" id="text" disabled="disabled">');
            out.appendTo(div);

            $('#morse').change(update);
            $('#morse').keypress(scheduleUpdate);
            $('#morse').bind('paste', scheduleUpdate);
        }
    }
})(jQuery);
