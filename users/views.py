from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponseForbidden, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from libnetid.http import login_url
import random
from django.urls import reverse
from django.conf import settings
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode


def return_from_ulb(request):
    sid, uid = request.GET.get("_sid", False), request.GET.get("_uid", False)

    if sid and uid:
        user = authenticate(sid=sid, uid=uid)
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next')
            if next_url:
                next_url = urlsafe_base64_decode(next_url).decode()
            else:
                next_url = reverse("me")
            return HttpResponseRedirect(next_url)

    return HttpResponseForbidden("Bad")


def login_view(request):
    return_url = "{base}{path}?next={next}".format(
        base=settings.BASE_URL,
        path=reverse("return_from_ulb"),
        next=urlsafe_base64_encode(request.GET.get('next', reverse("me")).encode()).decode()
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


@login_required
def me_json(request):
    return JsonResponse(request.user.as_dict())
