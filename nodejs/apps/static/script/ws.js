var _ws_url;
function ws_set_url(url){
    _ws_url=url;
}
var _ws_onBeforePost;
function ws_onBeforePost(callback){
    _ws_onBeforePost=callback;
}
var _ws_onAfterPost
function ws_onAfterPost(callback){
    _ws_onAfterPost=callback
}
function ws_call(path,params,cb){
    if(!cb)  { 
        cb=params;
        params=undefined
    }
    var sender=undefined;
    if(_ws_onBeforePost){
        sender=_ws_onBeforePost();
    }
    $.ajax({
        type: "POST",
        url: _ws_url,
        data:JSON.stringify({
            path:path,
            params:JSON.stringify(params)
        }),
        success: function(res,data){
            if(_ws_onAfterPost){
                _ws_onAfterPost(sender);
            }
            cb(undefined,res);
        },
        error:function(ex,txt){
            cb({message:txt})

        },
        dataType: 'json'
      });
}