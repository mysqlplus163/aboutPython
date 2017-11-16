
function a() {
  $.extend({
  dalong: function(arg){
    console.log("extend1");
    console.log(arg);
  }
});

function f1() {
  console.log("extend1 f1");
}

}

a()
