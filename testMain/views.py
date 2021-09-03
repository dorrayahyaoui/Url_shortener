from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from .models import *

def root(request, url_hash):
    url_ser = get_object_or_404(Url_service, short_url=url_hash)
    url_ser.clicked()
    return redirect(url_ser.url)
