(function (jq) {
  jq.extend({
    "GDP": function (arg, arg2) {
      // 绑定事件
      jq(arg).find(":submit").on("click", function () {
        var allInput = jq(arg).find("input");
        // 清空错误信息
        allInput.parent().removeClass("has-error");
        allInput.next().text("");
        // 校验
        allInput.each(function () {
          if (jq(this).attr("required")) {
            if (jq(this).val().length === 0) {
              showError(this, "不能为空");
            }
            console.log("不为空");
            var minLength = arg2[jq(this).attr("name")]["min-length"];
            console.log(minLength);
            if (minLength !== undefined) {
              if (jq(this).val().length < minLength) {
                showError(this, "不能低于"+minLength+"位");
              }
            }
          }
        });
        return false;
      });
    };

  function showError(ele, msg) {
    jq(ele).parent().addClass("has-error");
    var name = jq(this).prev().text();
    jq(this).next().text(name + msg);
    return false;
  }
  });
})(jQuery);