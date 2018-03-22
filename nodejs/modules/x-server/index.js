"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var Express = require("express");
var Consolidate = require("consolidate");
var E = Express();
var Application = (function () {
    function Application(name) {
        this.name = name;
        this.staticPath = "public";
        this.clientStatic = "static";
        this.tempatePath = "templates";
        this.viewEngine = {
            name: "pug",
            ext: "pug"
        };
    }
    return Application;
}());
exports.Application = Application;
function createApp(name, options) {
    var ret = new Application(name);
    if (options && options.viewEngine) {
        ret.viewEngine.name = options.viewEngine.name;
        ret.viewEngine.ext = options.viewEngine.ext;
    }
    return ret;
}
exports.createApp = createApp;
var _apps = [];
function find_app(url) {
}
function host(app, hostDir, appDir) {
    _apps.push(app);
    appDir = appDir || "apps";
    var appViewDir = appDir + "/" + app.name + "/" + app.tempatePath;
    if (app.name != "default") {
        app.clientStatic = app.name + "/" + app.clientStatic;
        app.staticPath = appDir + "/" + app.name + "/" + app.staticPath;
    }
    else {
        app.staticPath = +appDir + "/" + app.staticPath;
    }
    console.log(app);
    E.use("/" + app.clientStatic, Express.static(app.staticPath));
    var _consolidate = Consolidate;
    E.engine(app.viewEngine.ext, _consolidate[app.viewEngine.name]);
    E.set('views', "./apps");
    if (app.name != "default") {
        E.get("/" + (hostDir || app.name), function (req, res) {
            var _app = find_app(req.url);
            var x = Consolidate;
            console.log(app.viewEngine);
            x[app.viewEngine.name]("apps/" + app.name + "/" + app.tempatePath + "/index." + app.viewEngine.ext, {
                data: {
                    name: "XXX"
                }
            }, function (ex, html) {
                if (ex) {
                    res.end(ex.message || ex);
                }
                else {
                    res.end(html);
                }
            });
        });
    }
    else {
        E.get('/', function (req, res) {
            res.render("default/" + app.tempatePath + "/index.pug");
        });
    }
}
exports.host = host;
function run(port) {
    E.listen(port);
}
exports.run = run;
//# sourceMappingURL=index.js.map