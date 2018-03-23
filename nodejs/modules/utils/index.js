"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var url = require("url");
var _rootUrl;
function getFullUrl(req) {
    return url.format({
        protocol: req.protocol,
        host: req.get('host'),
        pathname: req.originalUrl
    });
}
exports.getFullUrl = getFullUrl;
function generateModel(params, cb) {
    if (!_rootUrl) {
        _rootUrl = getFullUrl(params.req);
        if (_rootUrl[_rootUrl.length - 1] === "/") {
            _rootUrl = _rootUrl.substring(0, _rootUrl.length - 1);
        }
    }
    var ret = {
        rootUrl: _rootUrl
    };
    ret.static = function (url) {
        return ret.rootUrl + "/static" + url;
    };
    ret.model = params.model;
    cb(null, ret);
}
exports.generateModel = generateModel;
//# sourceMappingURL=index.js.map