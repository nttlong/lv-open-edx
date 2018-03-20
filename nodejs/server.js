var req =require("./modules/ws");
req.set_url('http://localhost:8080//web_services/');
req.call("lv@get_user_db",{
            username: "nttlong",
            email:"nttlong@lacviet.com"
        }).then(res=>{
    console.log(res);
}).catch(ex=>{
    console.log(ex);
})
// try {
//     var ret=req.callSync("lv@get_list_of_students");    
// } catch (error) {
//     console.log("loi");
// }
