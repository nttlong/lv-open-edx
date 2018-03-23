import * as url from "url"
import {Request,Response} from "express"
var _rootUrl:string;
export function getFullUrl(req:Request):string{
    
    return url.format({
        protocol: req.protocol,
        host: req.get('host'),
        pathname: req.originalUrl
      });
}
export function generateModel(params:{req:Request,res:Response,model:any},cb:(ex?:any,res?:any)=>void):void {
    if(!_rootUrl){
        _rootUrl=getFullUrl(params.req)
        if(_rootUrl[_rootUrl.length-1]==="/"){
            _rootUrl=_rootUrl.substring(0,_rootUrl.length-1)
        }
    }
    var ret:any={
        rootUrl:_rootUrl
    }
    ret.static=function(url:string){
        return ret.rootUrl+"/static"+url
    }
    ret.model=params.model
    cb(null,ret);
}