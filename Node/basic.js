console.log("Hello World!");



function add(a,b){
    return a+b;
}

console.log("Hello js");

console.log(add(2,10));

console.log(process.argv);


var args = process.argv.slice(2);

console.log("Adding the numbers from the console",add(parseInt(args[0]), parseInt(args[1])));