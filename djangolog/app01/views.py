from django.shortcuts import render, HttpResponse

import logging
logger = logging.getLogger(__name__)
logger_collect = logging.getLogger("collect")
# Create your views here.


def author_list(request):
    logger.error("Authhhhhhhhhhhhh...")
    return HttpResponse("Author is OK.")


def publisher_list(request):
    logger_collect.info("Pubbbbbbbbbbbbb....")
    return HttpResponse("Publisher is OK.")


def book_list(request):
    logger.info("Bookkkkkkkkkkk....")
    return HttpResponse("Book is OK.")
