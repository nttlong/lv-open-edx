var req =require("./modules/ws");
req.set_url('http://0.0.0.0:8001/web_services/');
req.call("lv@create_course_manage",{
            org: "3333",
            course:"3333",
            display_name: "3333",
            run: "3333",
            codeteacher:"rootsang1"
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
