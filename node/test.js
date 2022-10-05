const path = require("path");

//console.log("hello world")

//const hello = "Hello from Node JS Variable"
//console.log(hello)

//console.log(`printing variable hello ${hello}`);

//console.log("directory name: " + __dirname);
//console.log("directory and file name: " + __filename) 

console.log("Using PATH module:");
console.log(`hello from file ${path.basename(__filename)}`);
console.log(`Process args: ${process.argv}`)


