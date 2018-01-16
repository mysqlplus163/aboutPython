var age;
function bar(age) {
  console.log(age);
  var age = 99;
  var sex = "male";
  console.log(age);
  function age() {
    alert(123);
  }
  console.log(age);
  return 100;
}
result = bar(5);
console.log(result);


function func() {
  console.log(age)
}
func();