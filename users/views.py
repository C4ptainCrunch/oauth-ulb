from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from libnetid.http import login_url
import random
from django.urls import reverse
from django.conf import settings


def return_from_ulb(request):
    sid, uid = request.GET.get("_sid", False), request.GET.get("_uid", False)

    if sid and uid:
        user = authenticate(sid=sid, uid=uid)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(request.GET.get('next', reverse("me")))

    return HttpResponseForbidden("Bad")


def login_view(request):
    return_url = "{base}{path}?next={next}".format(
        base=settings.BASE_URL,
        path=reverse("return_from_ulb"),
        next=request.GET.get('next', reverse("me"))
    )
    url = login_url(return_url)
    return HttpResponseRedirect(url.url)


def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def me(request):
    img = random.choice(["gazon", "r42", 'resto', 'panneau'])
    return render(request, 'me.html', {'image': img})
