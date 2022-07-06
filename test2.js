CryptoJS = require("crypto-js");  // npm install crypto-js
_0x189cbb = CryptoJS
function get_my_value(){
    token  = _0x456254("/api/movie");
    return token;
}
function base(m){
    let base1 = CryptoJS.enc.Utf8.parse(m)
        ,base2 = CryptoJS.enc.Base64.stringify(base1)
    return base2;
}
function _0x456254() {
            for (var _0x5da681 = Math['round'](new Date()['getTime']() / 0x3e8)['toString'](),
                     _0x2a83dd = arguments['length'], _0x31a891 = new Array(_0x2a83dd), _0x596a02 = 0x0;
                 _0x596a02 < _0x2a83dd;
                 _0x596a02++)
                _0x31a891[_0x596a02] = arguments[_0x596a02];
            _0x31a891['push'](_0x5da681);
            var _0xf7c3c7 = _0x189cbb['SHA1'](_0x31a891['join'](','))['toString'](_0x189cbb['enc']['Hex'])
              , _0x3c8435 = [_0xf7c3c7, _0x5da681]['join'](',')
                ,wordArray = CryptoJS.enc.Utf8.parse(_0x3c8435)
                ,base64 = CryptoJS.enc.Base64.stringify(wordArray)

    return base64
        }
        console.log(get_my_value())
