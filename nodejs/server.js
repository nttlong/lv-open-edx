var req =require("./modules/ws");

req.set_url('http://0.0.0.0:8000/search/');

req.call("course_discovery",{
            search_string:"sangtest",
            page_size:20,
            page_index:0
        }).then(res=>{
    console.log(res);
}).catch(ex=>{
    console.log(ex);
})
