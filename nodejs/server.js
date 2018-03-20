var req =require("./modules/ws");
req.set_url('http://0.0.0.0:8000/web_services/');
req.call("lv@get_list_of_students").then(res=>{
    console.log(res);
}).catch(ex=>{
    console.log(ex);
})
// try {
//     var ret=req.callSync("lv@get_list_of_students");    
// } catch (error) {
//     console.log("loi");
// }
