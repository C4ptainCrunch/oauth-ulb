from django.shortcuts import render, redirect


def home(request):
    if request.user.is_authenticated:
        return redirect('me')
    else:
        return render(request, 'home.html')
