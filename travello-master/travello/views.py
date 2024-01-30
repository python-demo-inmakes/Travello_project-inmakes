from django.shortcuts import render, redirect

# Create your views here.
from travello.models import Destination


def index(request):
    # dest1 = Destination()
    # dest1.name = 'Russia'
    # dest1.desc = 'Vladimir Putin Bitch!'
    # dest1.img = 'destination_1.jpg'
    # dest1.price = 500
    # dest1.offer = True
    #
    # dest2 = Destination()
    # dest2.name = 'North Korea'
    # dest2.desc = 'Kim Jon Un Bitch!'
    # dest2.img = 'destination_2.jpg'
    # dest2.price = 1000
    # dest2.offer = False
    #
    # dest3 = Destination()
    # dest3.name = 'USA'
    # dest3.desc = 'Donald Trump Bitch!'
    # dest3.img = 'destination_3.jpg'
    # dest3.price = 700
    # dest3.offer = False
    #
    # dests = [dest1, dest2, dest3]

    dests = Destination.objects.all()

    return render(request, 'index.html', {
        'dests': dests
    })


def destination(request, nme=None, id=None):
    # dests = Destination.objects.
    if id != None:
        dest = Destination.objects.get(id=id)
        # print(dest.name)
        return render(request, 'destination.html', {
            'dest': dest
        })
    return redirect('/')
