from django.shortcuts import render, redirect
import logging
from app01 import models

# Create your views here.

logger = logging.getLogger(__name__)


def login(request):
    if request.method == "POST":
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        logger.debug(user)
        logger.debug(pwd)
        if models.UserInfo.objects.filter(name=user, password=pwd):
            logger.info("{} is login.".format(user))
        else:
            logger.warning("{} loging failed.".format(user))
    
    logger.info("有人来登陆了")
    return render(request, "login.html")

