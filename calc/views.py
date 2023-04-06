from django.shortcuts import render,redirect
from .models import train_details
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.contrib import messages


# Create your views here.
def home_view(request):
    train =  train_details.objects.all()

    return render(request,'home.html',{'title':'Bangladesh Railway','courses':train})
    

def navbar_view(request):
    return render(request,'navbar.html',{'title':'navbar'})

def search_view(request):
    routes = {"1":"Dhaka","2":"Sylhet","3":"Madaripur"}
    if request.method =="GET":
        from_dest = request.GET['from']
        to_dest = request.GET['to']
        if from_dest.lower()=="select" or to_dest.lower()=="select":
            return redirect('/')
        
        
        #trains = train_details.objects.raw("SELECT * FROM train_details where start_dest="'+from_dest+'"and end_dest="'+to_dest+'")
        else:
            from_dest = routes[from_dest]
            to_dest = routes[to_dest]
            #trains = train_details.objects.raw("SELECT * FROM train_details")
            #trains = train_details.objects.raw('SELECT * FROM train_details WHERE start_dest=%s AND to_dest=%s',[from_dest,to_dest])
            trains = train_details.objects.filter(Q(start_dest=from_dest) & Q(end_dest=to_dest))
            return render(request, 'search.html',{'trains':trains,'from_dest':from_dest})
        '''if from_dest =="1":
            from_dest= "Dhaka"
            return render(request,'search.html',{"train":"This is 1"})
        elif from_dest =="2":
            from_dest = "Sylhet"
            return render(request,'search.html',{"train":"This is Dhaka"})
        else:
            from_dest = "Madaripur"
            return render(request,'search.html',{"train":from_dest})
        #to_dest = request.GET['to']
        #train_class = request.GET['class']
        search ="Hi"'''
        '''if search =="":
            return render(request,'search.html',{'searched':'Nothing','courses':[]})
        else:
            trains = train_details.objects.filter(from__contains=from_dest)
            if trains:
                return render(request,'search.html',{'searched':search,'courses':trains})

            else:
                return render(request,'search.html',{'searched':search,'no_result':'No result found'})
    else:
        return render(request,'search.html',{})'''

def tickets_view(request):
    trains = train_details.objects.raw("SELECT * FROM train_details")
    return render(request,'tickets.html',{'trains':trains,"title":"Tickets"})


def add_tickets(request):
    return render(request,'add.html',{'title':'Add'})


def added_tickets(request):
    routes = {"1":"Dhaka","2":"Sylhet","3":"Madaripur"}
    if request.method =="POST":
        from_dest = request.POST['from']
        to_dest = request.POST['to']
        if from_dest.lower()=="select" or to_dest.lower()=="select":
            return redirect('/')
        
        
        #trains = train_details.objects.raw("SELECT * FROM train_details where start_dest="'+from_dest+'"and end_dest="'+to_dest+'")
        else:
            from_dest = routes[from_dest]
            to_dest = routes[to_dest]
            id = request.POST['id']
            train_name = request.POST['name']
            price = request.POST['price']
            seat = request.POST['seat']
            date = request.POST['date']
            if train_details.objects.filter(train_id=id).exists():
                messages.info(request,'This ID already exists')
                return redirect('add')
            else:
                train = train_details.objects.create(train_id = id,train_name=train_name,train_class="First",seat_status=seat,available_date =date,start_dest=from_dest,end_dest=to_dest,price = price)
                train.save()
    return render(request,'added.html')
            
            
            
