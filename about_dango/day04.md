# modal框版编辑班级信息 学生信息

把前面的例子都改成模态框修改的方式


1. 班级表属于单表操作

2. 学生表属于一对多操作


## 知识点

jQuery知识点

js阻止默认事件提交 => return false;

location.reload() => 刷新当前页

后端：json.dumps()
前端：JSON.parse()



```javascript
$.ajax({
  url: "",
  type: "POST",
  data: {"nid": nid, "content": content},
  success:function(arg){
    // arg字符串类型
    // JSON.parse(字符串) => 对象
    // JSON.stringify(对象) => 字符串
    console.log(arg);
    argObj = JSON.parse(arg);
    if (argObj.status){
      // 跳转到
      location.href = "/class_list/"
      // 刷新当前页
      location.reload();
    }else{
      // ...
    }
  }
})
```