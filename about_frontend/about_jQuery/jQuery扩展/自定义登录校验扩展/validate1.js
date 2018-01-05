"use strict";
(function (jq) {
  jq.extend({
    validate: function () {
      jq("form :submit").on("click", function () {
      // 清空error信息
      jq(".error").text("");
      var flag = true;
      jq("form input[type='text'], form input[type='password']").each(function () {
        // 遍历
        var $currInput = jq(this);
        console.log($currInput.val().length === 0);
        if ($currInput.val().length === 0) {
          var currNamr = $currInput.parent().text();
          $currInput.next("span").text(currNamr + "不能为空");
          flag = false;
          return false;
        }
      });
      return flag;
    });
    }
  });
})(jQuery);
