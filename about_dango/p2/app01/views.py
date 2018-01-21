from django.shortcuts import render, HttpResponse

# Create your views here.


def blog(request):
    res = HttpResponse("<h1>OK</h1>")
    print(res.charset)
    print(res.content)
    print(res.status_code)
    print(res.status_code)
    print(res["Content-Type"])
    return res


def template_test(request):
    l = [11, 22, 33]
    d = {"name": "alex"}
    s = "你 好 啊 世 界"
    st = "<script>alert(123);</script>"

    class Person(object):
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def dream(self):
            return "{} is dream...".format(self.name)

    Alex = Person(name="Alex", age=34)
    Egon = Person(name="Egon", age=9000)
    Eva_J = Person(name="Eva_J", age=18)

    person_list = [Alex, Egon, Eva_J]
    return render(request, "template_test.html", {"l": l, "d": d, "person_list": person_list, "s": s, "st": st})


def login(request):
    return render(request, "login.html")
