/**
 * Created by liwenzhou on 2016/8/19.
 */
// 上线页面step1的自定义验证

function validateForm() {
    $("#submit_form").validate({
        rules: {
            // 模式的select选择框
            mode_select: {
                required: true
            }

        }
    })
}