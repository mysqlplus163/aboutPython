(function (jq) {
  jq.fn.extend({
    validate: function (arg) {
      var $this = $(this);
      console.log($this);
      $this.find(":submit").on("click", function () {
      // 清空error信息
      $this.find(".error").text("");
      var flag = true;
      $this.find("input[type='text'], input[type='password']").each(function () {
        // 遍历
        var $currInput = jq(this);
        console.log($currInput.attr("name"));
        var inputName = $currInput.attr("name");
        var inputValue = $currInput.val();
        if (arg !== undefined && arg[inputName] !== undefined && arg[inputName].required) {
          console.log("required-->", inputName);
          if (inputName === "mobile"){
            var mobileP = /1[3|5|6|8]\d{9}/;
             if (mobileP.test(inputValue)){
               console.log("是正常的手机号");
             }else {
               console.log("格式不对");
             }
          }
        }
        // console.log($currInput.val().length === 0);
        // if ($currInput.val().length === 0) {
        //   var currNamr = $currInput.parent().text();
        //   $currInput.next("span").text(currNamr + "不能为空");
        //   flag = false;
        //   return false;
        // }
      });
      return false;
    });
    }
  })
})(jQuery);
