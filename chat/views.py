from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect
from chat.models import Msg
from django.urls import reverse
from datetime import datetime
# Create your views here.


def index(request):
    msgList = get_list_or_404(Msg.objects.order_by('id'))
    return render(request, 'chat/index.html', {'msgList': msgList})

def posting(request):
    newMsg = Msg()
    newMsg.words = str(request.POST['usermsg'])
    newMsg.pub_date = datetime.today()
    newMsg.save()
    return HttpResponseRedirect(reverse('chat:index'))