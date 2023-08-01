from django.shortcuts import render
from .models import Room
# from django.http import HttpResponse


# rooms = [
#     {'id': 1, 'name': 'Lets learn python'},
#     {'id': 2, 'name': 'Design with me'},
#     {'id': 3, 'name': 'Frontend developers'},
# ]


def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    # return HttpResponse('Home page')
    return render(request, 'base/home.html', context)


def room(request, pk):
    room = Room.objects.get(id=pk)

    context = {'room': room}
    # return HttpResponse('ROOM')
    return render(request, 'base/room.html', context)

# Create your views here.
