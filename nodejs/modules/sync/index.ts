import * as DEASYNC from "deasync";
export var sync=<T>(fn:any, args:Array<any>, cb?:(error:any,ret:any)=>void):T=> {
    function reject(e:any):void {

        result = {
            error: e
        };
    };
    function resolve(r:any):void {
        result = {
            result: r
        };
    }
    if (args instanceof Array) {
        var result:any = undefined;
        var _cb = function (e:any, r:any) {
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


        }
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