CryptoJS = require('crypto-js');
var encryptByDES = function(t) {
            var e="e9284d45-cf2a-4e46-9367-f122413ca6b0"
            var a = CryptoJS.enc.Utf8.parse(e);
            try {
                var s = CryptoJS.DES.encrypt(String(t), a, {
                    mode: CryptoJS.mode.ECB,
                    padding: CryptoJS.pad.Pkcs7
                })
            } catch (t) {
                console.log(t)
            }
            return s.toString()

        }
console.log(encryptByDES("zl1301673843"))

