from django.shortcuts import render, redirect
from .models import Room, Topic
from .forms import RoomForm
# from django.http import HttpResponse

# from django.http import HttpResponse


# rooms = [
#     {'id': 1, 'name': 'Lets learn python'},
#     {'id': 2, 'name': 'Design with me'},
#     {'id': 3, 'name': 'Frontend developers'},
# ]


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    rooms = Room.objects.filter(topic__name__icontains=q)

    topics = Topic.objects.all()

    context = {'rooms': rooms, 'topics': topics}
    # return HttpResponse('Home page')
    return render(request, 'base/home.html', context)


def room(request, pk):
    room = Room.objects.get(id=pk)

    context = {'room': room}
    # return HttpResponse('ROOM')
    return render(request, 'base/room.html', context)


def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html', context)


def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html',  context)


def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    # print(str(pk))
    if request.method == 'POST':
        # print(request.POST)
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html')

# def deleteRoom(request, pk):
#     print("pk:", pk)
#     try:
#         room = Room.objects.get(id=pk)
#         print("room:", room)
#     except Room.DoesNotExist:
#         print("Room does not exist.")
#         # return HttpResponse("Room not found.", status=404)
#     return render(request, 'base/delete.html')
    # Rest of the view function...
