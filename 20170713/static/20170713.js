/**
 * Created by Q1mi on 2017/7/13.
 */

// swal({
//   title: "你确定要删除这条记录吗？",
//   text: "删除之后就找不回来咯！",
//   type: "warning",
//   showCancelButton: true,
//   confirmButtonColor: "#f22b00",
//   confirmButtonText: "删吧，我想好了",
//   closeOnConfirm: false
// },
// function(){
//   swal("Deleted!", "Your imaginary file has been deleted.", "success");
// });


function test1() {
    $("#a1").click(function () {
        swal({
          title: "你确定要删除这条记录吗？",
          text: "删除之后就找不回来咯！",
          type: "warning",
          showCancelButton: true,
            cancelButtonText: "取消",

          confirmButtonColor: "#f22b00",
          confirmButtonText: "删吧，我想好了",
          closeOnConfirm: false
        },
            // 点击确认按钮之后会执行下面的这个匿名函数
        function(){
            /* 在这里写一些业务逻辑*/

          swal("删除成功！", "你要删除的小片儿都删除了。。。祝你幸福", "success");
        });
    })
}

function test2() {
   $("#a2").click(function () {
       swal({
               title: "Are you sure?",
               text: "You will not be able to recover this imaginary file!",
               type: "warning",
               showCancelButton: true,
               confirmButtonColor: "#DD6B55",
               confirmButtonText: "Yes, delete it!",
               cancelButtonText: "No, cancel plx!",
               closeOnConfirm: false, //因为有二级的确认页面，所以这里写false
               closeOnCancel: false
           },
           function (isConfirm) {
               if (isConfirm) {
                   swal("Deleted!", "Your imaginary file has been deleted.", "success");
               } else {
                   swal("Cancelled", "Your imaginary file is safe :)", "error");
               }
           });
   });
}


function deleteorder(orderid) {
    swal({
        title: "Are you sure?",
        text: "Are you sure that you want to cancel this order?",
        type: "warning",
        showCancelButton: true,
        closeOnConfirm: false,
        confirmButtonText: "Yes, cancel it!",
        confirmButtonColor: "#ec6c62"
    }, function () {
        $.ajax(
            {
                type: "get",
                url: "/admin/delete_order.php",
                data: "orderid=" + orderid,
                success: function (data) {
                }
            }
        )
            .done(function (data) {  // 成功取消时的提示
                swal("Canceled!", "Your order was successfully canceled!", "success");
                $('#orders-history').load(document.URL + ' #orders-history');
            })
            .error(function (data) {  // 取消失败时的提示
                swal("Oops", "We couldn't connect to the server!", "error");
            });
    });
}

$(function () {
    test1();
    test2();
});