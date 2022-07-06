const jsdom = require("jsdom");
const { JSDOM } = jsdom;
const NewjsDom = new JSDOM(`<!DOCTYPE html><p>Hello Lx</p>`);
const window = NewjsDom.window;
const document = NewjsDom.document
function sign(){
    return window.origin
}