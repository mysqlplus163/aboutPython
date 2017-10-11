# jQuery

## 为什么要学jQuery?

面试题的例子，你们的长我的短，领导就喜欢短的。总有另类的人嘛

两个比较（学生写的和老师写的） 引出来为什么要用jQuery。


我们的代码本质上是实现了一样的功能，不过我用的是模块导入，内部帮我实现了一些功能。这个模块叫jQuery。
我们今后一般都是使用jQuery的。

## 什么是jQuery？
一个JS库（类似于模块， Python中叫模块，JS中就叫类库）。
JS和jQuery的区别？我们以后都用jQuery为什么还要学JS。

还是拿Python中的模块来举例，我们会了Python就可以自己写模块，但是为了使用方便我们就直接用别的写好的模块，不用重复造轮子。
就类似我们之前学Bootstrap框架，Bootstrap里面那些样式我们自己都会写，为什么还用Bootstrap呢？就是方便、就是省事儿。


## jQuery版本和使用
    - 导入模块 -> 导入js文件
      就像Python中的re模块一样，它里面有很多的方法，类似re.match。
      那jQuery中也是有很多写好的方法，我们只需要使用jQuery.xx来使用，又因为每次都写jQuery.xx太长了，所以起了个别名叫$来等效替换jQuery，所以以后我们一般都是用$.xx来使用jQuery里面的方法。

    - 版本介绍
      1.x 2.x 和 3.x
      考虑到兼容IE8的画 推荐使用1.x的版本
      如果不考虑老旧的IE的话，我们就推荐使用3.x的版本

      压缩版本和未压缩版本
      压缩的用于线上生产环境，减少网络消耗
      未压缩版本通常用于学习使用


## jQuery知识点，jQuery这个模块里都有那些东西呢？

我们学的前端那些知识点，无非就是基于以下内容：
   HTML，CSS，JS

   HTML：裸体的人
   CSS：让人穿上衣服
   JS：让人动起来


   动起来指的是什么呢？
        给金鑫带上绿帽子
        让谁和谁拼刺刀
        我的短，找到谁比我还短
        不仅要找到短的，还要找到扎人的那个。。。

   本质：-> 找到谁 让谁做点什么
        - 找
            - 直接找
                $("#id")  身份证号是多少的那个人
                $(".class")  头上带绿帽子的人
                $("div")，按分类找 找男人 找女人 可能还有狗呢，对吧，xxx
                $("*") 动物世界(找到所有)
                $(".class, div")  头上带绿帽子的人和狗

                出题：10～15道题，给一个HTML页面让学生找
                    1.
                    2.
                    3.
                    4.
                    ...

            - 间接找
                $("爸爸 子子孙孙")
                $("爸爸>儿子")
                $("黄衣服+蓝衣服")  我们要找的是蓝衣服的，黄衣服后面的蓝衣服
                $("黄衣服～蓝衣服")  黄衣服身边的蓝衣服的

                出题：10
                    html，找
                    1。
                    2。
                    3。

            - 其他选择器：
                。。。


            筛选器：
            例子：
                左侧菜单onclick=func(this)
                。。
                。。
                。。

            总结：
                常用的那10-15

        - 属性
            属性
                attr(name|pro|key,val|fn)
                removeAttr(name)
                prop(n|p|k,v|f)
                removeProp(name)
                全选
                    - 找到所有checkbox，每个都选中
                    - 问：$(":checkbox")
                    - 循环，一个一个设置$(this).prop("true")  -> 对不对？
                    其实不用，直接选择器后面跟prop(true)就行
                    - $(":checkbox").prop("true")
                    记住啦！对jQuery查找到的一系列标签；做统一操作的话就可以直接做动作就行
                    ============
                取消
                    让学生带着老师写...

                    ============
                反选
                    - 统一操作行不行？
                    - 已经选中的，给它取消；没有选中的，给它选中 引入坑。。。

                    上面不行，只能用循环来做了，根据每个checkbox的状态来反向操作

                    - 循环
                        - 使用for循环来实现
                        - 接着引出each循环，重点介绍下this

                总结：（全选反选这个例子，我们学到了什么？）
                    - 统一操作，直接写动作  -> $("checked").prop("false")
                    - each循环
            CSS 类
                addClass(class|fn)
                removeClass([class|fn])
                toggleClass(class|fn[,sw])

                例子：
                    开关（一个灯泡，变黄变灰）
            HTML代码/文本/值
                html([val|fn])
                text([val|fn])
                val([val|fn|arr])

                一个参数和两个参数的区别

                # 写下面的例子
                1. input，搜索框，请输入关键字的例子
                2. select，多选的情况- > val是列表，设置的时候也要是列表
                3. checkbox，radio 获取值

                =====================
                内部插入
                    append(content|fn)
                    appendTo(content)
                    prepend(content|fn)
                    prependTo(content)
                例子：
                    ul标签里面，前插一行，后插一行
                    <ul>
                       <li>
                    </ul>

                外部插入
                    after(content|fn)
                    before(content|fn)
                    insertAfter(content)
                    insertBefore(content)

                例子：
                    表格，增加行（前插一行，后插一行）

                外部插入
                    after(content|fn)
                    before(content|fn)
                    insertAfter(content)
                    insertBefore(content)
                包裹
                    wrap(html|ele|fn)
                    unwrap()

                    wrapAll(html|ele)
                    wrapInner(html|ele|fn)
                替换
                    replaceWith(content|fn)
                    replaceAll(selector)
                删除
                    empty()
                    remove([expr])
                复制
                    clone([Even[,deepEven]])
                    搜索，+

                CSS
                    css(name|pro|[,val|fn])1.9*
                    +效果

                位置
                    offset([coordinates])
                    position()
                    scrollTop([val])
                    scrollLeft([val])
                    返回顶部
                尺寸
                    height([val|fn])
                    width([val|fn])
                    innerHeight()
                    innerWidth()
                    outerHeight([soptions])
                    outerWidth([options])


        例子：
            左侧菜单

            点开之后，下面的菜单定位到最下面（练习位置）



事件：
    问，之前学到哪些绑定事件的方法？
        1. onclick=func  每个标签都要手写
        2. element.onclick=function(){// 事件处理代码}
        3. element.addEventListener("click", function(){})  -> 事件冒泡

        弊端：批量绑定事件

    jQuery，目标：xxxx
        $().click();

        例子：
            - 左侧菜单：this

        onchange
            - 鼠标拖动的例子

    练习题：表格
        html
        1. 应该输入，按钮
        2. 删除，绑定，删除
        和学生一起写，争取带入坑里

        等写完了然后说：有BUG，让学生找。。。请吃饭

        引出：
            事件委托
            delagate()

        小总结：
            click() 这种用于绑定事件的
            delegate() 这种用于给未来的标签（绑定事件后添加的html）绑定事件的。
        我们应该用什么呢？

        都不对
        我们用下面讲的这个。
        引出
            - on()

        大总结：
        把所有的绑定事件的方式总结一下：
            - JS
                - onclick=func
                - .onclick=function(){// 事件处理代码}
                - addEventListener（事件冒泡）
            - jQuery
                - click
                - delegate
                - on
    我们学会了绑定事件，那我们应该什么时候绑定事件？
    引出
            $(document).ready(function(){
                    ...
            });

            $(function(){
                ...
            });


动画：
    - 基本
    - 滑动
    - 淡入淡出
    - 自定义


插件：
    用 表单验证 的例子一步一步引出来：
    如何做成一个插件
        - 自执行函数

课后练习题：
    1. 登陆+验证
    2. 左侧菜单
    3. 表格，增加，编辑，删除
    4. 表格，增加，编辑，删除 + 验证 【可选】
