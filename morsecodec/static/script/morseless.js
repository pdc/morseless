var Morseless = (function($) {
    var ajaxUrl;
    var out;

    function update() {
        var morse = $('#morse').val();
        $.getJSON(ajaxUrl, {morse: morse}, function (data, textStatus, jqXHR) {
            out.val(data.text);
        });
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

        }
    }
})(jQuery);
