from django.db import models

# Create your models here.


class Auth(models.Model):
    url=models.CharField(max_length=64,verbose_name='权限URL',blank=True, null=True)
    title=models.CharField(max_length=32,verbose_name='权限标题',blank=True, null=True)
    code_choices=(
        (1,'add'),
        (2,'sel'),
        (3,'edi'),
        (4,'del')
    )
    tag=models.IntegerField(choices=code_choices)
    is_title=models.BooleanField(verbose_name='是不是菜单')

    @property
    def tag_choice(self):
        return self.get_tag_display()

    class Meta:
        verbose_name_plural = '权限表'
        
    def __str__(self):
        return self.title
    
    
class UserInfo(models.Model):
    username=models.CharField(verbose_name='用户名',max_length=32,blank=True,null=True)
    password=models.CharField(verbose_name='密码',max_length=64,blank=True,null=True)
    Ctime=models.DateTimeField(verbose_name='创建时间',auto_now_add=True)
    name = models.CharField(verbose_name='人名', max_length=16, blank=True, null=True)
    email = models.EmailField(verbose_name='邮箱', max_length=64, blank=True, null=True)
    roles=models.ManyToManyField(to='Role')

    class Meta:
        verbose_name_plural='用户表'
        
    def __str__(self):
        return self.username
    

class Role(models.Model):
    name = models.CharField(verbose_name='角色名', max_length=32, blank=True, null=True)
    auths = models.ManyToManyField(to='Auth')
