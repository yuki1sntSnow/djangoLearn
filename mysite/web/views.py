from django.shortcuts import render
from web import models

def mysqlConnet(request):
    infoList = models.objects.all()
    return render(request, "mysqlConnect.html", {"infoList":infoList})