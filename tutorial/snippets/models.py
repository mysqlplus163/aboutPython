from django.db import models

# Create your models here.

from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Snippet(models.Model):

    created = models.DateTimeField(auto_now_add=True, verbose_name=u"创建时间")
    title = models.CharField(max_length=100, blank=True, default="", verbose_name=u"标题")
    code = models.TextField(verbose_name=u"代码")
    linenos = models.BooleanField(verbose_name=u"代码行号", default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=100, default="python", verbose_name=u"语言")
    style = models.CharField(choices=STYLE_CHOICES, max_length=32, default="friendly", verbose_name=u"样式")
    owner = models.ForeignKey("auth.User", related_name="snippets", on_delete=models.CASCADE)
    highlighted = models.TextField(verbose_name=u"高亮")

    class Meta:
        ordering = ("created", )
        verbose_name = "代码片段"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{}".format(self.created)

    def save(self, *args, **kwargs):
        """
        使用‘pygments’库去创建一个高亮的html表示的代码片段
        :return:
        """
        lexer = get_lexer_by_name(self.language)
        linenos = self.linenos and "table" or False
        options = self.title and {"title": self.title} or {}
        formatter = HtmlFormatter(
            style=self.style,
            linenos=linenos,
            full=True,
            **options
        )
        self.highlighted = highlight(self.code, lexer, formatter)
        super(Snippet, self).save(*args, **kwargs)
