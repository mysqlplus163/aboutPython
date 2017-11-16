(function (jq) {
  jq.extend({
    "GDP": function (arg) {
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
              jq(this).parent().addClass("has-error");
              var name = jq(this).prev().text();
              jq(this).next().text(name + "不能为空");
              return false;
            }
          }

        });
        return false;
      });
    }
  });
})(jQuery);