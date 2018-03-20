import * as request from "request"
var _url:string;
function fn_error(cb,reject,ex){
    if(cb) cb(ex);
    else reject(ex);
}
function fn_res(cb,resolve,res){
    if(cb) cb(null,res);
    else resolve(res);
}
export function set_url(strUrl:string){
    _url=strUrl;
}
export function call(path:string,data?:any,cb?:(error?:any,result?:any)=>void):Promise<any>{
    return new Promise((resolve,reject)=>{
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