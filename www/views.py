from django.shortcuts import render
import random


def home(request):
    img = random.choice(["gazon", "r42", 'resto', 'panneau'])
    return render(request, 'home.html', {'image': img})
