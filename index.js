// var fs = require('fs');
// const {VM,VMScript} = require('vm2');
// const file = `${__dirname}/1.js`;
// const windowfile = `${__dirname}/window.js`;
// const vm = new VM();
// const script = new VMScript(fs.readFileSync(windowfile)+fs.readFileSync(file),"调试");
// debugger;
// vm.run(script);
// debugger;
const {VM, VMScript} = require('vm2');
const fs = require('fs');
const file = `${__dirname}/1.js`;

// By providing a file name as second argument you enable breakpoints
const script = new VMScript(fs.readFileSync(file), file);

new VM().run(script);
