function ff() {
  $.extend({
  dalong1: function(){
    f1();
  }
});

function f1() {
  console.log("extend1 f1");
}
}

ff();
