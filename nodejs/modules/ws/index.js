"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var request = require("request");
var DEASYNC = require("deasync");
exports.sync = function (fn, args, cb) {
    function reject(e) {
        result = {
            error: e
        };
    }
    ;
    function resolve(r) {
        result = {
            result: r
        };
    }
    if (args instanceof Array) {
        var result = undefined;
        var _cb = function (e, r) {
            if (e) {
                result = {
                    error: e
                };
            }
            else {
                result = {
                    result: r
                };
            }
        };
        args.push(_cb);
        fn.apply(fn, args);
        DEASYNC.loopWhile(function () {
            return result === undefined;
        });
        if (result.error) {
            throw (result.error);
        }
        else {
            return result.result;
        }
    }
    else {
        var result = undefined;
        fn({
            resolve: resolve,
            reject: reject,
        });
        DEASYNC.loopWhile(function () {
            return result === undefined;
        });
        if (result.error) {
            throw (result.error);
        }
        else {
            return result.result;
        }
    }
};
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
function callSync(path, data) {
    function run(cb) {
        call(path, data).then(function (res) {
            cb(null, res);
        }).catch(function (ex) {
            cb(ex);
        });
    }
    try {
        var ret = exports.sync(run, []);
        return ret;
    }
    catch (ex) {
        throw (ex);
    }
}
exports.callSync = callSync;
//# sourceMappingURL=index.js.map