const server=require("./modules/x-server");
var app=server.createApp("admin",{
    viewEngine:{
        name:"lodash",
        ext:"html"
    }
});
var hrm=server.createApp("hrm");
server.host(app);
server.host(hrm);
server.run(3000);