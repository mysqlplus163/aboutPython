from django.shortcuts import render, redirect
import logging
from app01 import models

# Create your views here.

son_logger = logging.getLogger("app01.views.son")


def index(request):
    son_logger.info("in view2 .........")
    return render(request, "index.html")
