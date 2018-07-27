function wsUploadFile(){
    var me=this;
    me.setFileContent=function(data){
        me._fileContent=data;
        return me;
    };
    me.setApi=function(apiPath){
        me._api=apiPath;
        return me;
    };
    me.setData=function(data){
        me._data=data;
        return me;
    };
    me.setViewPath=function(path){
        me._viewPath=path;
        return me;
    };
    me.doUpload=function(callback){
        var now = new Date();
        var offset_minutes = now.getTimezoneOffset();
        var sender=undefined;
        if(_wsOnBeforeCall){
            sender=_wsOnBeforeCall();
        }
         $.ajax({
            url: ws_get_url(),
            type: "post",
//            dataType: "json",
//            data: {
//                fileContent:me._fileContent,
//                path:me._api,
//                data:JSON.stringify({
//                   path:me._api,
//                   view:me._viewPath,
//                   data:me._data,
//                   offset_minutes:offset_minutes
//                })
//            } ,
            success: function (res) {

                if(_wsOnAfterCall){
                    _wsOnAfterCall(sender)
                }
               if(cb){
                    cb(undefined,res)
               }
               else{
                    resolve(res)
               }

            },
            error: function(jqXHR, textStatus, errorThrown) {
                if(_wsOnAfterCall){
                    _wsOnAfterCall(sender)
                }
                var newWindow = window.open();
                var txt=jqXHR.responseText
                while(txt.indexOf(String.fromCharCode(10))>-1){
                    txt=txt.replace(String.fromCharCode(10),"<br/>")
                }
                newWindow.document.write(txt);
                if(cb){
                    cb({
                        error:{
                            type:"server"
                        }
                    })
                }
                else {
                reject({
                        error:{
                            type:"server"
                        }
                    })}

            }
        });
    };


}