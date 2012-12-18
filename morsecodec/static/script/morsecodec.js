

window.Morse = (function () {
    var fromMorse = {
        '/': ' ',
        "-.--": "Y",
        "--..--": ",",
        "....-": "4",
        ".-..-.": "\"",
        "-.-.-.": ";",
        "-...": "B",
        "-..-": "X",
        ".-.": "R",
        "--.-": "Q",
        "--..": "Z",
        ".--": "W",
        ".-.-.": "+",
        "..---": "2",
        ".-": "A",
        "..": "I",
        "-.-.": "C",
        "---...": ":",
        "..--.-": "_",
        "-": "T",
        ".": "E",
        ".--.-.": "@",
        ".-..": "L",
        "--.": "G",
        "...": "S",
        "..-": "U",
        "...-..-": "$",
        "..--..": "?",
        ".----": "1",
        "-.-.--": "!",
        ".--.": "P",
        "-----": "0",
        "-.-": "K",
        "-..": "D",
        "----.": "9",
        "-....": "6",
        "-...-": "=",
        ".---": "J",
        "---": "O",
        ".-.-.-": ".",
        "--": "M",
        "---..": "8",
        "-.": "N",
        "....": "H",
        ".----.": "'",
        "...-": "V",
        "--...": "7",
        ".....": "5",
        "...--": "3",
        "-....-": "-",
        "..-.": "F"
    };

    return {
        // Given a string in Morse code, return a string in plaintext.
        decode: function (morse) {
            var parts = morse.split(/\s+/);
            var text = '';
            for (var i = 0; i < parts.length; ++i) {
                var c = fromMorse[parts[i]];
                text += (c == null ? ' ' + parts[i] + ' ' : c);
            }
            return text;
        },

        // Search within this element for statches of morse code and translate.
        decodeElement: function (elt) {
            var text = '';
            for (var e = elt.firstChild; e; e = e.nextSibling) {
                if (e.nodeType == 1) {
                    // Element
                    this.decodeElement(e);
                } else if (e.nodeType == 3) {
                    // Text
                    var morse = e.nodeValue;
                    if (morse.match(/[.-][.-]/)) {
                        // Contains morse code maybe
                        text += this.decode(morse) + '\n';
                    }
                }
            }
            text = text.replace(/^\s*(.*)\s*$/, '$1');
            if (text.match('^UU:')) {
                text = text.toLowerCase().replace(/u/g, 'U');
            }
            if (text !== '') {
                elt.setAttribute('title', text);
            }
        }
    }
})();