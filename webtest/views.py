from django.shortcuts import render


def index(request):
    return render(request, "index.html", context={'text': 'Hello'})


def room(request):
    return render(request, 'room.html', context={'text1': 'Hello1', 'text2': 'hello2', 'text3': 'hello3'})
