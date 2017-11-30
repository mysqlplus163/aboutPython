$(document).ready(function () {
  $("#modal-submit").on("click", function () {
    var className = $("#inputclassname2").val();
    $.ajax({
      url: "/modal_add_class/",
      data: {"class_name": className},
      type: "post",
      success: function (data) {
        if (data === "OK") {
          location.href = "/class_list/"
        } else {
          $("#modal-error").text(data).parent().parent().addClass("has-error");
        }
      }
    })
  });
  // 给表格中每一行的编辑按钮绑定事件，点击弹出模态框
  $("table .m-edit").on("click", function () {
    // 显示模态框
    $("#myEditModal").modal("show");
    // 给编辑模态框赋值
    var $tds = $(this).parent().parent().children();
    var classID = $tds.eq(0).text();
    var className = $tds.eq(1).text();
    $("#editClassID").val(classID);
    $("#editClassName").val(className);
  });

  // 给编辑模态框的提交按钮绑定事件
  $("#myEditModal").find(".m-submit").on("click", function () {
    // 先清空错误信息
    $("input+span").text("").parent().parent().removeClass("hide");
    // 获取class_id 和class_name
    var classID = $("#myEditModal").find("input[name='class_id']").val();
    var className = $("#myEditModal").find("input[name='class_name']").val();
    $.ajax({
      url: "/modal_edit_class/",
      type: "post",
      data: {"class_id": classID, "class_name": className},
      success: function (data) {
        console.log(data);
        var dataObj = JSON.parse(data);
        if (dataObj.status === 0) {
          // 表示后端更新成功了
          // 刷新页面
          location.href = "/class_list/";
        } else {
          // 更新失败
          $("#myEditModal").find("input[name='class_name']").next().text(dataObj.msg).parent().parent().addClass("has-error");
        }
      }
    })
  });

  // swal删除
  $("table .swal-delete").on("click", function () {
    var classID = $(this).parent().parent().children().first().text();
    swal({
      title: "确定要删除这个班级吗？",
      text: "删除后可就无法恢复了。",
      type: "warning",
      showCancelButton: true,
      closeOnConfirm: false,
      confirmButtonText: "是的，我要删除！",
      confirmButtonColor: "#ec6c62",
      cancelButtonText: "容我三思"
    }, function (isConfirm) {
      if (!isConfirm) return;
      $.ajax({
        type: "post",
        url: "/modal_delete_class/",
        data: {"class_id": classID},
        success: function (data) {
          var dataObj = $.parseJSON(data);
          if (dataObj.status === 0) { //后端删除成功
            swal("删除成功", dataObj.msg, "success");
            console.log("class-" + classID);
            $("#class-" + classID).remove();
          } else {
            swal("出错啦。。。", dataObj.msg, "error");  //后端删除失败
          }
        },
        error: function () {  // ajax请求失败
          swal("啊哦。。。", "服务器走丢了。。。", "error");
        }
      })
    });
  });
});