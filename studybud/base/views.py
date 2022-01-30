from django.shortcuts import render

# Create your views here.
rooms= [
    
]


def home(request):
    return render(request, 'home.html')

def room(request):
    return render(request, 'room.html')
