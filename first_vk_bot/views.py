from django.shortcuts import render
from django.http import HttpResponse
from .forms import IdForm, MessageForm, InviteForm, SignUpForm
from .vk_help import get_friends, send_message, invite_to_group, save_fotos
import time
import requests
from django.contrib.auth import authenticate
import os


def index(request):
    return render(request, "index.html")



def send_message_(request):
    if request.method == "POST":
        id_ = request.POST.get("id")
        msg = request.POST.get("msg")
        if request.user.is_authenticated:
            token=request.user.token
            ids=get_friends(token, id_)
            for id in ids:
                send_message(token, id, msg)
                time.sleep(3)
        messageform = MessageForm()
        return render(request, "send_message.html", {"form": messageform})
    else:
        messageform = MessageForm()
        return render(request, "send_message.html", {"form": messageform})

def invite(request):
    if request.method == "POST":
        id_ = request.POST.get("id")
        id_group = request.POST.get("id_group")
        if request.user.is_authenticated:
            token = request.user.token
            ids=get_friends(token, id_)
            for id in ids:
                invite_to_group(token, id_group, id)
                time.sleep(3)
        inviteform = InviteForm()
        return render(request, "invite.html", {"form": inviteform})
    else:
        inviteform = InviteForm()
        return render(request, "invite.html", {"form": inviteform})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            #user = authenticate(username=username, password=raw_password)
            #login(request, user)

            return render(request, "index.html")
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def save_photos(request):
    if request.method == "POST":
        id_ = request.POST.get("id")
        if request.user.is_authenticated:
            token = request.user.token
            photos=save_fotos(token, id_)
            imgs=[]
            for photo in photos:
                dict= photo['attachment']['photo']
                del dict['album_id']
                del dict['date']
                del dict['id']
                del dict['owner_id']
                del dict['has_tags']
                del dict['access_key']
                del dict['height']
                del dict['text']
                del dict['width']
                keys=list(dict.keys())
                razm=[]
                for key in keys:
                    razm.append(int(key[6:]))
                imgs.append(photo['attachment']['photo']['photo_{}'.format(max(razm))])

            os.mkdir(id_)
            i=0
            for img in imgs:
                p = requests.get(img)
                out = open("{}/img{}.jpg".format(id_,i), "wb")
                out.write(p.content)
                out.close()
                i+=1

        inviteform = IdForm()
        return render(request, "invite.html", {"form": inviteform})
    else:
        inviteform = IdForm()
        return render(request, "invite.html", {"form": inviteform})


