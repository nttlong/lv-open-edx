import * as Express from "express";
import * as Consolidate from "consolidate";
import * as PATH from "path";
var E=Express();
export class Application {
    public staticPath:string;
    public clientStatic:string;
    public name:string;
    public tempatePath:string;
    public viewEngine:{
        name:string,
        ext:string
    };
    constructor(name:string){
        this.name=name;
        this.staticPath="public";
        this.clientStatic="static";
        this.tempatePath="templates";
        this.viewEngine={
            name:"pug",
            ext:"pug"
        }
    }

}
export function createApp(name:string,options?:{
    viewEngine?:{
        name:string,
        ext:string
    }
    
}):Application {
    var ret=new Application(name);
    if(options && options.viewEngine){
        ret.viewEngine.name=options.viewEngine.name;
        ret.viewEngine.ext=options.viewEngine.ext;
        
    }
    
    return ret;
}
var _apps:Array<Application>=[]
function find_app(url:string):Application{
    
}
export function host(app:Application,hostDir?:string,appDir?:string){
    _apps.push(app);
    appDir=appDir||"apps";
    var appViewDir=appDir+"/"+app.name+"/"+app.tempatePath;
    if(app.name!="default"){
        app.clientStatic=app.name+"/"+app.clientStatic;
        app.staticPath=appDir+"/"+app.name+"/"+app.staticPath;
        
    }
    else {
       
        app.staticPath=+appDir+"/"+app.staticPath;
        
    }
    console.log(app);
    E.use("/"+app.clientStatic, Express.static(app.staticPath));
    var _consolidate:any=Consolidate;
    E.engine(app.viewEngine.ext, _consolidate[app.viewEngine.name]);
    
    E.set('views',"./apps");
    if(app.name!="default"){
        E.get("/"+(hostDir||app.name),(req,res)=>{
            var _app=find_app(req.url);
            var x:any=Consolidate;
            console.log(app.viewEngine)
            x[app.viewEngine.name]("apps/"+app.name+"/"+app.tempatePath+"/index."+app.viewEngine.ext,{
                data:{
                    name:"XXX"
                }
            },(ex:any,html:string)=>{
                if(ex){
                    res.end(ex.message||ex);

                }
                else {
                    res.end(html);

                }
                
            })
            
        })
    }
    else{
        E.get('/', function(req, res){
            res.render("default/"+app.tempatePath+"/index.pug");
         });
    }
    
}   
export function run(port:number){
    E.listen(port)
}