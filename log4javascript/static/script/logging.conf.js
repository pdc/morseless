/*
* Set up logging
*
* Requires:
*     log4javascript.js
*/

window.log = (function () {
    var log = log4javascript.getLogger('frontend');

    var csrfToken = (function () {
        function getCookie(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie != '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = jQuery.trim(cookies[i]);
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) == (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }
        return getCookie('csrftoken');
    })();

    var ajaxAppender = new log4javascript.AjaxAppender('/logs/frontend');
    ajaxAppender.setSendAllOnUnload(true);
    ajaxAppender.setWaitForResponse(true);
    ajaxAppender.setLayout(new log4javascript.JsonLayout(true, false));
    ajaxAppender.setThreshold(log4javascript.Level.DEBUG);
    ajaxAppender.addHeader('X-CSRFToken', csrfToken);
    log.addAppender(ajaxAppender);

    return log;

})();
