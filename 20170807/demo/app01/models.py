from django.db import models

# Create your models here.


class Activity(models.Model):
    name = models.CharField(max_length=32, verbose_name="活动名称")
    start = models.IntegerField(verbose_name="开始时间", default=None)
    end = models.IntegerField(verbose_name="结束时间", default=None)
    notification = models.CharField(max_length=32, verbose_name="活动公告")
    type_choice = (
        ("invite", "邀请"),
        ("share", "分享"),
        ("play", "牌局"),
    )
    type = models.CharField(max_length=32, verbose_name="活动类型", choices=type_choice)
    # 活动条件可以有个，也就是一个活动对应多个活动条件
    conditions = models.ManyToManyField("")
    # 活动奖励, 可以有多种奖励
    rewards = models.ManyToManyField("Reward")
    daily_max = models.IntegerField(verbose_name="每日奖励物品上限", default=None)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "活动"
        verbose_name_plural = verbose_name


class Reward(models.Model):
    type_choice = (
        ("card", "房卡"),
        ("gold", "金币"),
        ("item", "道具"),
    )
    type = models.CharField(max_length=32, verbose_name="奖励类型", choices=type_choice)
    num = models.IntegerField(verbose_name="奖励数量", default=None)
    # 要加逻辑，确保id有值时 type==item
    id = models.IntegerField(verbose_name="道具ID", default=None)


    
    def __str__(self):
        return self.
        
    class Meta:
        verbose_name = "活动奖励"
        verbose_name_plural = verbose_name
         