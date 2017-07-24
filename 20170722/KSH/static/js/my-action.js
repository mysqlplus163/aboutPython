/**
 * Created by liwenzhou on 2017/7/23.
 */

$(function () {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    //删除记录
    function deleteRecord(recordID) {
        swal({
            title: "确定要删除这个产品吗？",
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
                url: "/delete/",
                data: {"id": recordID},
                success: function (data) {
                    var d_obj = $.parseJSON(data);
                    if (d_obj.code === "success") { //后端删除成功
                        swal("删除成功", d_obj.info, "success");
                        $("#p-" + recordID).remove()  //删除页面中那一行数据
                    } else {
                        swal("出错啦。。。", d_obj.info, "error");  //后端删除失败
                    }
                },
                error: function () {  // ajax请求失败
                    swal("啊哦。。。", "服务器走丢了。。。", "error");
                }
            })
        });
    }

    //新增产品提交
    function addProduct() {
        $.ajax({
            type: "post",
            url: "/add/",
            data: {
                "name": $("#inputName").val(),
                "status": $("#inputStatus").val(),
                "date": $("#inputDate").val()
            },
            success: function (data) {
                console.log(data);
                var d_obj = $.parseJSON(data);
                if (d_obj.code === "success") { //后端添加成功
                    swal("添加成功", d_obj.info, "success");
                    var html = '<tr id="p-' + d_obj.id + '" p-id="' + d_obj.id + '">';
                    html += '<td>' + d_obj.id + '</td>';
                    html += '<td>' + d_obj.name + '</td>';
                    html += '<td>' + d_obj.date + '</td>';
                    html += '<td>' + d_obj.status + '</td>';
                    html += '<td><a>' + '删除' + '</a></td>';
                    html += '</tr>';

                    $("#t1 tbody").append(html);  //在表哥最后添加一行数据
                } else {
                    swal("出错啦。。。", d_obj.info, "error");  //后端添加失败
                }
            },
            error: function () {  // ajax请求失败
                swal("啊哦。。。", "服务器走丢了。。。", "error");
            }
        })
    }

    //绑定点击事件
    $("#t1 tbody tr td a").click(function () {
        var id = $(this).parent().parent().attr("p-id");
        deleteRecord(id);
    });

    //绑定添加按钮事件
    $("#addButton").click(function () {
        addProduct();
    });

    //datetime picker
    $('#inputDate').datetimepicker({
        language: "zh-CN",
        format: 'yyyy-mm-dd hh:ii',
        autoclose: true,
        todayBtn: true
    });
});

