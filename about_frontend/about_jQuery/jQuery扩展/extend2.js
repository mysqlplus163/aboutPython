$.extend({
  dalong2: function(arg){
    f1();
    console.log("extend2");
    console.log(arg);
  }
});

function f1() {
  console.log("extend2 f1");
}