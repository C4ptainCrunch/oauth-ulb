from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.contrib.auth import authenticate, login


def ulb_auth(request):
    sid, uid = request.GET.get("_sid", False), request.GET.get("_uid", False)

    if sid and uid:
        user = authenticate(sid=sid, uid=uid)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')

    return HttpResponseForbidden("Bad")
