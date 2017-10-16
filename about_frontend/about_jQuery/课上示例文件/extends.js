
// $.extend({
//   "GDP": function(arg){
//     func1();
//     console.log("我爱" + arg);
//   }
// });
//
//
// function func1() {
//   console.log("我是GDP");
// }


// a = function (jq) {
//   jq.extend({
//   "GDP": function(arg){
//     func1();
//     console.log("我爱" + arg);
//   }
// });
//
//
// function func1() {
//   console.log("我是GDP");
// }
//
// };
//
// a(jQuery);


(function (jq) {
  jq.extend({
    "GDP": function(arg){
      func1();
      console.log("我爱" + arg);
    }
  });


  function func1() {
    console.log("我是GDP");
  }
})(jQuery);