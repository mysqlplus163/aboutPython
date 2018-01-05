"use strict";
(function ($) {
  function check() {
    // 定义一个标志位，表示验证通过还是验证不通过
    var flag = true;
    var errMsg;
    // 校验规则
    $("form input[type!=':submit']").each(function () {
      var labelName = $(this).prev().text();
      var inputName = $(this).attr("name");
      var inputValue = $(this).val();
      if ($(this).attr("required")) {
        // 如果是必填项
        if (inputValue.length === 0) {
          // 值为空
          errMsg = labelName + "不能为空";
          $(this).next().text(errMsg);
          flag = false;
          return false;
        }
        // 如果是密码类型，我们就要判断密码的长度是否大于6位
        if (inputName === "password") {
          // 除了上面判断为不为空还要判断密码长度是否大于6位
          if (inputValue.length < 6) {
            errMsg = labelName + "必须大于6位";
            $(this).next().text(errMsg);
            flag = false;
            return false;
          }
        }
        // 如果是手机类型，我们需要判断手机的格式是否正确
        if (inputName === "mobile") {
          // 使用正则表达式校验inputValue是否为正确的手机号码
          if (!/^1[345678]\d{9}$/.test(inputValue)) {
            // 不是有效的手机号码格式
            errMsg = labelName + "格式不正确";
            $(this).next().text(errMsg);
            flag = false;
            return false;
          }
        }
      }
    });
    return flag;
  }

  function clearError(arg) {
    // 清空之前的错误提示
    $(arg).next().text("");
  }
  // 上面都是我定义的工具函数
  $.extend({
    validate: function () {
      $("form :submit").on("click", function () {
      return check();
    });
    $("form :input[type!='submit']").on("focus", function () {
      clearError(this);
    });
    }
  });
})(jQuery);