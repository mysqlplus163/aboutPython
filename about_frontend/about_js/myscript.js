"use strict";
/**


 **/
var a = [10, 20, 30, 40]
for (var i=0;i<a.length;i++) {
  console.log(i);
}

// 单行注释
/*
* 多行注释
*/

// 普通函数定义
function f1() {
  console.log("Hello world!");
}

// 带参数的函数
function f2(a, b) {
  console.log(arguments);  // 内置的arguments对象
  console.log(arguments.length);
  console.log(a, b);
}

// 带返回值的函数
function sum(a, b){
  return a + b;
}
sum(1, 2);  // 调用函数

// 匿名函数方式
var sum = function(a, b){
  return a + b;
}
sum(1, 2);

// 立即执行函数
(function(a, b){
  return a + b;
})(1, 2);

var city = "BeiJing";
function f() {
  var city = "ShangHai";
  function inner(){
    var city = "ShenZhen";
    console.log(city);
  }
  inner();
}

var city = "BeiJing";
function Bar() {
  console.log(city);
}
function f() {
  var city = "ShangHai";
  return Bar;
}
var ret = f();
ret();  // 打印结果是？


var city = "BeiJing";
function f(){
    var city = "ShangHai";
    function inner(){
        console.log(city);
    }
    return inner;
}
var ret = f();
ret();


var person=new Object();
person.name="Alex";
person.age=18;


//方法1：不指定参数
var d1 = new Date();
console.log(d1.toLocaleString());
//方法2：参数为日期字符串
var d2 = new Date("2004/3/20 11:12");
console.log(d2.toLocaleString());
var d3 = new Date("04/03/20 11:12");
console.log(d3.toLocaleString());
//方法3：参数为毫秒数
var d3 = new Date(5000);
console.log(d3.toLocaleString());
console.log(d3.toUTCString());

//方法4：参数为年月日小时分钟秒毫秒
var d4 = new Date(2004,2,20,11,12,0,300);
console.log(d4.toLocaleString());  //毫秒并不直接显示



//RegExp对象

//创建正则对象方式1
// 参数1 正则表达式
// 参数2 验证模式：g(global)和i(忽略大小写)

// 用户名只能是英文字母、数字和_，并且首字母必须是英文字母。长度最短不能少于6位 最长不能超过12位。

// 创建RegExp对象方式
var reg1 = new RegExp("^[a-zA-Z][a-zA-Z0-9_]{5,11}$", "g");

// 匹配响应的字符串
var s1 = "bc123";

//RegExp对象的test方法，测试一个字符串是否符合对应的正则规则，返回值是true或false。
reg1.test(s1);  // true

// 创建方式2
// /填写正则表达式/匹配模式
var reg2 = /^[a-zA-Z][a-zA-Z0-9_]{5,11}$/g;

reg2.test(s1);  // true



// String对象与正则结合的4个方法
var s2 = "hello world";

s2.match(/o/g);         // ["o", "o"]             查找字符串中 符合正则 的内容
s2.search(/h/g);        // 0                      查找字符串中符合正则表达式的内容位置
s2.split(/o/g);         // ["hell", " w", "rld"]  按照正则表达式对字符串进行切割
s2.replace(/o/g, "s");  // "hells wsrld"          对字符串按照正则进行替换

// 关于模式：g和i的简单示例
var s1 = "name:Alex age:18";

s1.replace(/a/, "哈哈哈");      // "n哈哈哈me:Alex age:18"
s1.replace(/a/g, "哈哈哈");     // "n哈哈哈me:Alex 哈哈哈ge:18"      全局匹配
s1.replace(/a/gi, "哈哈哈");    // "n哈哈哈me:哈哈哈lex 哈哈哈ge:18"  不区分大小写

location.href   // 获取URL
location.href="URL"; // 重定向
location.reload(); // 重新加载页面
location="https://www.sogou.com";  // 跳转到