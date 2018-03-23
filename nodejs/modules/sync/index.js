"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
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
//# sourceMappingURL=index.js.map