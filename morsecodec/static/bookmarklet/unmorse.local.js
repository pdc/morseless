/*
* Load morse codec and translate morse-code fragments.
*
* This is designed to be run as a bookmarklet.
* See <http://morseless.me.uk/> for information.
*
* © 2012 Damian Cugley
*/

(function () {
    // Load a single script and call nextFunc when it is loaded.
    function loadOneScript(url, nextFunc) {
        var s = document.createElement('script')
        s.type = 'text/javascript';
        s.src =  url;
        s.onload = nextFunc;
        document.body.appendChild(s);
    }

    // Load the scripts in the list, and when they are all
    // loaded call finalFunc.
    function loadScripts(urls, finalFunc) {
        if (urls.length === 0) {
            finalFunc();
        }
        var url = urls.shift();
        loadOneScript(url, function () {
            loadScripts(urls, finalFunc);
        });
    }

    loadOneScript('http://localhost:8000/static/script/morsecodec.js',
        function () {
            Morse.decodeElement(document.body);
        });
})();