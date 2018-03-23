var express = require('express')
var utils=require("./modules/utils")
var app = express()
var cons = require('consolidate');
var req_ws =require("./modules/ws");
var sync=require("./modules/sync")
var path=require("path")
req_ws.set_url('http://0.0.0.0:8000/web_services/');
function create_sender(req,res){
    return {
        req:req,
        res:res
    }
}
app.get('/', function (req, res) {
    req.url
    var m=require(path.join(__dirname,"apps/controllers/index.js"))
    if(m){
        var retModel= sync.sync(m.load,[create_sender(req,res)])
        var dataModel=sync.sync(utils.generateModel,[{req:req,res:res,model:retModel}])
        res.render('index',dataModel);
    }
    else {
        var dataModel=sync.sync(utils.generateModel,[{req:req,res:res,model:retModel}])
        res.render('index',dataModel);
    }
})
app.get('/config', function (req, res) {
    
    try {
        var ret=req_ws.callSync("configs_info@get_info")
        res.end(JSON.stringify(ret))
    } catch (ex) {
        res.end(ex.message||ex);
        
    }
    
})
app.use("/static", express.static("apps/static"));
app.engine("ejs", cons.ejs);
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'apps/views'));
app.listen(3200)
console.log("http://localhost:3200")