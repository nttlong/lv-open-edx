"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var request = require("request");
var _url;
function fn_error(cb, reject, ex) {
    if (cb)
        cb(ex);
    else
        reject(ex);
}
function fn_res(cb, resolve, res) {
    if (cb)
        cb(null, res);
    else
        resolve(res);
}
function set_url(strUrl) {
    _url = strUrl;
}
exports.set_url = set_url;
function call(path, data, cb) {
    return new Promise(function (resolve, reject) {
        try {
            request.post(_url, {
                json: true,
                body: {
                    path: path,
                    params: (data) ? JSON.stringify(data) : undefined
                }
            }, function (ex, response, body) {
                if (ex) {
                    fn_error(cb, reject, ex);
                }
                else {
                    fn_res(cb, resolve, body);
                }
            });
        }
        catch (ex) {
            fn_error(cb, reject, ex);
        }
    });
}
exports.call = call;
//# sourceMappingURL=index.js.map