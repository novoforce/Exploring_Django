from django.shortcuts import render

# Create your views here.
rooms= [
    {'id':1,"name":"lets learn python"},
    {'id':2,"name":"lets learn Deep learning"},
    {'id':3,"name":"lets learn computer vision"}
]


def home(request):
    context= {'rooms': rooms}
    return render(request, 'base/home.html',context) #send the rooms list to the home.html

def room(request,pk):
    room= None

    for i in rooms:
        if i['id']==int(pk):
            room= i
    context= {'room':room}
    print("--> ",context)
    return render(request, 'base/room.html',context)
