from django.shortcuts import render
from .models import Destination

# Create your views here.


def index(request):

    dest1 = Destination()
    dest1.img ='destination_2.jpg'
    dest1.name = 'Mumbai'
    dest1.desc = 'The City Never Sleeps'
    dest1.price =750
    dest1.offer = False

    dest2 = Destination()
    dest2.name ='Lagos'
    dest2.img ='destination_4.jpg'
    dest2.desc = 'The City Always Busy'
    dest2.price = 800
    dest2.offer = True


    dest3 = Destination()
    #dest3.name ='London'
    #dest3.desc = 'The Digital WorkPlace'
    #dest3.img ='destination_1.jpg'
    #dest3.price = 850
    #dest3.offer = False

    #dest4 = Destination()
    #dest4.name ='Vancouver'
    #dest4.desc = 'The Beautiful City'
    #dest4.img ='destination_3.jpg'
    #dest4.price = 690
    #dest4.offer = False

    #dest5 = Destination()
    #dest5.name ='Paris'
    #dest5.desc = 'The Most Beautiful City In The World'
    #dest5.img ='destination_6.jpg'
    #dest5.price = 830
    #dest5.offer = False

    #dest6 = Destination()
    #dest6.name ='New York'
    #dest6.desc = 'The Most Loved City In The World'
    #dest6.img ='destination_5.jpg'
    #dest6.price = 900
    #dest6.offer = True

    #dests =[dest1 ,dest2,dest3,dest4,dest5,dest6]

    dests = Destination.objects.all() 

    return render(request , "index.html" , {'dests':dests }  )

