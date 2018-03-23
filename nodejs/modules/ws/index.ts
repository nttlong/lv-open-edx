import * as request from "request"
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
var _url:string;
function fn_error(cb:any,reject:any,ex:any){
    if(cb) cb(ex);
    else reject(ex);
}
function fn_res(cb:any,resolve:any,res:any){
    if(cb) cb(null,res);
    else resolve(res);
}
export function set_url(strUrl:string){
    _url=strUrl;
}
export function call(path:string,data?:any,cb?:(error?:any,result?:any)=>void):Promise<any>{
    return new Promise<any>((resolve,reject)=>{
        try {
            request.post(_url,{
                    json: true,
                    body:{
                        path:path,
                        params:(data)?JSON.stringify(data):undefined
                    }
                
                }, function (ex, response, body) {
                    if(ex){
                       fn_error(cb,reject,ex)
                    }
                    else {
                       fn_res(cb,resolve,body)
                    }
                    
                    
                    
                })
        } catch (ex) {
            fn_error(cb,reject,ex);
            
        }
    })
}
export function callSync(path:string,data?:any):any{
    function run(cb:any){
        call(path,data).then(res=>{
            cb(null,res);
        }).catch(ex=>{
            cb(ex);
        })
    }
    try {
        var ret=sync(run,[]);
        return ret;    
    } catch (ex) {
        throw(ex)
    }
    
}