var CryptoJS = require('crypto-js');
window = {}
_0x4e96b4 = window;
_$Tk = CryptoJS;
_0x4e96b4['_$is'] =new Date()['valueOf']()['toString']()
_0x4e96b4['_$qF'] = CryptoJS['enc']['Utf8']['parse'](btoa(_0x4e96b4['_$is'])['slice'](0x0, 0x10));
_0x4e96b4['_$pr'] = ['083a1fa83f345a560bfbc5a8f744a27c', '8a50835ab137c3ffcbaecbba882edb99', 'ee3d0d1b4c2107bc6f1076228e49a53d', '809362fab014d50487a8a1567e1559f8', '9b3035713610937936081ac963a2729e']
//_$pr会改变吗？
_$Ww = _$Tk['enc']['Utf8']['parse'](_0x4e96b4['_$pr']['toString']()),
_0x29dd83 = _$Tk['AES']['encrypt'](_$Ww, _0x4e96b4["_$qF"], {
'mode': _$Tk['mode']['ECB'],
'padding': _$Tk['pad']['Pkcs7']
}),
_0x4e96b4['_$ss'] = _0x29dd83['toString']();
console.log(_0x4e96b4['_$ss'])

