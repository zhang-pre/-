
    mt.cookie = {};
    mt.cookie.set = function(e, a, b) {
        var f;
        b.D && (f = new Date,
        f.setTime(f.getTime() + b.D));
        document.cookie = e + "=" + a + (b.domain ? "; domain=" + b.domain : "") + (b.path ? "; path=" + b.path : "") + (f ? "; expires=" + f.toGMTString() : "") + (b.dc ? "; secure" : "")
    }
    ;
    mt.cookie.get = function(e) {
        return (e = RegExp("(^| )" + e + "=([^;]*)(;|$)").exec(document.cookie)) ? e[2] : u
    }
    ;
    mt.cookie.sb = function(e, a) {
        try {
            var b = "Hm_ck_" + +new Date;
            mt.cookie.set(b, "42", {
                domain: e,
                path: a,
                D: s
            });
            var f = "42" === mt.cookie.get(b) ? "1" : "0";
            mt.cookie.set(b, "", {
                domain: e,
                path: a,
                D: -1
            });
            return f
        } catch (d) {
            return "0"
        }
    }
    ;