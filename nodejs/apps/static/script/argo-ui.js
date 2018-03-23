var argo_ui = angular.module("argo-ui", []);
argo_ui.directive("editorText", ["$parse", function ($parse) {
    return {
        restrict: "CEA",
        template: "<input type='text' class=\"form-control input-sm\" />",
        replace: true,
        link: function (scope, ele, attr) {
           
        }
    }
}]);
argo_ui.directive("editorPassword", ["$parse", function ($parse) {
    return {
        restrict: "CEA",
        template: "<input type='password' class=\"form-control input-sm\" />",
        replace: true,
        link: function (scope, ele, attr) {

        }
    }
}]);
argo_ui.directive("editorDate", ["$parse", function ($parse) {
    return {
        restrict: "CEA",
        template: '<div class="input-group date" data-provide="datepicker">'+
    '<input type="text" class="form-control input-sm">'+
    '<div class="input-group-addon">'+
        '<span class="glyphicon glyphicon-th"></span>'+
    '</div>'+
'</div>',
        replace: true,
        link: function (scope, ele, attr) {
           
            $(ele[0]).datepicker({
                format: attr.format||'mm/dd/yyyy',
                startDate: '-3d'
            });
            if (attr.ngModel) {
                var date = scope.$eval(attr.ngModel);
                $(ele[0]).data().datepicker.setDate("2017-11-20")
            }
        }
    }
}]);
argo_ui.service("$render", ["$http", "$compile", function ($http, $compile) {
    function loadUrl(url, cb) {
        $http({
            method: "GET",
            url: url
        }).then(function (response) {
            cb(undefined, response.data);
        }, function (error) {
            cb(error);
        });
    }
    var retService= {
        load: function (url, cb) {
            loadUrl(url, cb);
        
        },
        loadTemplateTo: function (url, ele, cb) {
            var scope = angular.element(ele).scope();
            loadUrl(url, function (err, html) {
                if (err) {
                    cb(err);
                    return;
                }
                var ret = $compile($("<div>"+html+"</div>").contents())(scope);
                $(ret[0]).appendTo($(ele)[0]);
                cb(undefined, ret);
            })
        },
        loadPage: function (url,  cb) {
            loadUrl(url, function (e, h) {

                if (e) {
                    cb(e);
                    return;
                }
                var ret = {
                    scripts:[]
                };
                ret.template = h;
                debugger;
                var bScript = h.indexOf("<script>")
                while(bScript > -1) {
                    bScript +=  "<script>".length;
                    var eScript = h.indexOf("</script>", bScript);
                    var scriptContent = h.substring(bScript, eScript);
                    ret.scripts.push(scriptContent);
                    ret.template = h.replace("<script>" + scriptContent + "</script>", "");
                    bScript = h.indexOf("<script>", eScript);
                }
                cb(undefined, ret);
            });
        },
        loadPageTo: function (url, ele, cb) {
            retService.loadPage(url, function (e, r) {
                if (e) {
                    cb(e);
                    return;
                }
                var scope = angular.element(ele).scope();
                var subScope = scope.$new(true, scope);
                if (r.scripts) {
                    for (var i = 0; i < r.scripts.length; i++) {
                        var fn = Function("var ret=" + r.scripts[i] + ";return ret");
                        fn()(subScope);
                    }
                }
                var retEle = $("<div>" + r.template + "</div>");
                var ret = $compile(retEle.contents())(subScope);
                ret.appendTo(ele);
                cb(undefined, ret);
                function watch() {
                    if (!$.contains(document.body, ret[0])) {
                        debugger;
                        subScope.$destroy();
                    }
                    else {
                        setTimeout(watch, 1000);
                    }
                };
                watch();
            });
        }
    }
    return retService;
}]);
argo_ui.service("$history", [function () {
    function history_navigator($scope) {
        var oldUrl;
        function historyMonitorStart(handler) {
            function run() {
                if (oldUrl != window.location.href) {

                    if (historyChangeCallback.length > 0) {
                        if (window.location.href.indexOf('#') > -1) {
                            var data = {};
                            var url = window.location.href.split('#')[1];
                            var items = url.split('&');
                            var ret = {};
                            for (var i = 0; i < items.length; i++) {
                                data[items[i].split('=')[0]] = decodeURI(window["unescape"](items[i].split('=')[1]));
                            }
                            for (var i = 0; i < historyChangeCallback.length; i++) {
                                historyChangeCallback[i](data);
                            }
                            var keys = Object.keys($scope.$history.events);
                            for (var i = 0; i < keys.length; i++) {
                                if (!$scope.$history.events[keys[i]].hasStartCall) {
                                    var obj = {
                                        key: keys[i],
                                        data: data,
                                        done: function () {
                                            if ($scope.$history.events[obj.key])
                                                $scope.$history.events[obj.key].handler(obj.data);
                                        }
                                    }
                                    setTimeout(function () {
                                        obj.done();
                                    }, 300);

                                }
                            }

                        }
                        else {
                            historyChangeCallback[historyChangeCallback.length - 1]({});
                        }
                    }
                    oldUrl = window.location.href;
                }
                setTimeout(run, 100);
            }
            run();
        }

        var historyChangeCallback = [];
        function applyHistory(scope) {

            scope.$history = {
                isStart: true,
                events: {},
                data: function () {
                    if (window.location.href.indexOf('#') == -1)
                        return {};
                    var url = window.location.href.split('#')[1];
                    var items = url.split('&');
                    var ret = {};
                    for (var i = 0; i < items.length; i++) {
                        ret[items[i].split('=')[0]] = decodeURI(window["unescape"](items[i].split('=')[1]));
                    }
                    return ret;
                },
                change: function (callback) {
                    var _data = scope.$history.data();
                    callback(_data);
                    scope.$$$$historyCallback = callback;
                    historyChangeCallback.push(callback);

                },
                redirectTo: function (bm) {
                    window.location.href = bm;
                },
                onChange: function (subScope, handler) {

                    scope.$history.events["scope_" + subScope.$id] = {
                        handler: handler,
                        hasStartCall: true,
                        scope: subScope
                    };
                    subScope.$on("$destroy", function () {
                        delete scope.$history.events["scope_" + subScope.$id];
                    });
                    if (scope.$history.events["scope_" + subScope.$id].hasStartCall) {
                        handler(scope.$history.data());
                        scope.$history.events["scope_" + subScope.$id].hasStartCall = false;
                    }

                }
            };
            function URLObject(obj) {
                obj.$url = this;
                var me = this;
                me.data = obj.$history.data();
                me.clear = function () {
                    me.data = {};
                    return me;
                };
                me.item = function (key, value) {
                    if (!me.data) {
                        me.data = {};
                    }
                    me.data[key] = value;
                    return me;
                };
                me.done = function () {
                    var keys = Object.keys(me.data);
                    var retUrl = "";
                    for (var i = 0; i < keys.length; i++) {
                        retUrl += keys[i] + "=" + window["escape"](encodeURI(me.data[keys[i]])) + "&";
                    }
                    retUrl = window.location.href.split('#')[0] + '#' + retUrl.substring(0, retUrl.length - 1);
                    return retUrl;
                };
                var x = 1;
            }
            new URLObject(scope);
            historyMonitorStart(historyChangeCallback);
        }
        return new applyHistory($scope);
    }
    return {
        apply: function (scope) {
            history_navigator(scope);
        }
    }
}]);
argo_ui.directive("subPage", ["$render", function ($render) {
    return {
        restrict: "CEA",
        link: function (scope, ele, attr) {
            attr.$observe("url", function (val) {
                $(ele[0]).empty();
                if (angular.isUndefined(val)) return;
                $render.loadPageTo(val, ele, function (e, r) {
                    if (e) {
                        if ((!e.data) || (e.data === "")) {
                            $("<div>" + e.statusText + "</div>").appendTo(ele[0]);
                        }
                        else {
                            $("<div>" + e.data + "</div>").appendTo(ele[0]);
                        }
                    }
                  
                });
                
            })
        }
    }
}]);
argo_ui.service("$callback", ["$http", function ($http) {
    function create(name) {
        if (!argo_ui.$$$services) {
            argo_ui.$$$services = {};
        }
        argo_ui.$$$services[name] = {};
        var me = this;
        me.setUrl = function (url) {
            argo_ui.$$$services[name].url = url;
            return me;
        };
        me.getUrl = function () {
            return argo_ui.$$$services[name].url;
        };
        me.onBeforeCall = function (cb) {
            argo_ui.$$$services[name].onBeforeCall = cb;
            return me;
        };
        me.onAfterCall = function (cb) {
            argo_ui.$$$services[name].onAfterCall = cb;
            return me;
        };
        me.caller = function (scope) {
            function ret() {
                var _me = this;
                _me._scope = scope;
                _me.done = function (data, cb) {
                    var sender;
                    if (argo_ui.$$$services[name].onBeforeCall) {
                        sender = argo_ui.$$$services[name].onBeforeCall();
                    }
                    var config = {
                        //headers: {
                        //    'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8;'
                        //}
                    }

                    $http.post(me.getUrl(), data, config)
                        .then(function (data, status, headers, config) {
                            if (argo_ui.$$$services[name].onAfterCall) {
                                argo_ui.$$$services[name].onAfterCall(sender);
                            }
                            var res = data.data;
                            cb(undefined, res);
                        }, function (data, status, header, config) {
                            if (argo_ui.$$$services[name].onAfterCall) {
                                argo_ui.$$$services[name].onAfterCall(sender);
                            }
                            cb(data, undefined)
                        });
                }
            };
            return new ret();
        }
    }
    return function (name) {
        return new create(name);
    }
}])