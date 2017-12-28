var p = new RegExp("^[a-z]{2,3}$", "g");

var s1 = "name:Alex age:18";

s1.replace(/a/, "哈哈哈");
s1.replace(/a/g, "哈哈哈");
s1.replace(/a/gi, "哈哈哈");


console.log(p.test());
console.log(p.test());
