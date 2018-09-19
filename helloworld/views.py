# -*- coding: utf-8 -*-
import socket
from django.http import HttpResponse
def index(request):
    return HttpResponse(socket.gethostname())
