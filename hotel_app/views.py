from datetime import datetime
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from .models import*
from django.contrib.auth import authenticate,login,logout





# Create your views here.
def home(request):
    return HttpResponse("Heyy")

def base(request):
    return render(request, 'base.html')

def index(request):
    room = Rooms.objects.all()
    context ={
        'room':room
    } 
    return render(request, 'index.html',context)

def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')


def room(request):
    room = Rooms.objects.all()
    context ={
        'room':room
    }
    return render(request, 'room.html',context)


def booking(request):
    return render(request,'booking.html')

def ourteam(request):
    return render(request, 'team.html')

def testimonial(request):
    return render(request, 'testimonial.html')

def contact(request):
    return render(request, 'contact.html')

# def signup(request):
#     if request.method== 'POST':
#         username=request.POST['username']
#         email=request.POST['email']
#         print(email)
#         password=request.POST['password']
#         password1=request.POST['confirm_password']
#         if password==password1:
#             if User.objects.filter(username=username).exists():
#                 messages.info(request, 'Username already exists')
#                 return render(request, 'signup.html')
#             elif User.objects.filter(email=email).exists():
#                 messages.info(request, 'Email already exists')
#                 return render(request, 'signup.html')
#             else:
#                 user=User.objects.create_user(username=username, email=email, password=password1)
#                 user.save()
#                 messages.info(request, 'User created')
#                 return render(request, 'login.html')
#         else:
#             messages.info(request, 'Password not matched')
#             return redirect('signup')
#         print('valid mail',email)    
#     return render(request,"signup.html")



# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = auth.authenticate(username=username, password=password)
#         if user is not None:
#             auth.login(request, user)
#             return redirect('index')
#         else:
#             messages.info(request, 'Invalid credentials')
#             return redirect('login')
#     return render(request, 'login.html')

# def logout(request):
#     auth.logout(request)
#     return redirect('login')


           
       
def admin(request):
    return render(request, 'adminhome.html')

def add_room(request):
    
    if request.method == 'POST':
       rno=request.POST['roomno']
       des=request.POST['des']
       ac=request.POST['ac']
       type=request.POST['type']
       bed=request.POST['bed']
       rate=request.POST['rate']
       img=request.FILES['img']
       addRoom = AddRoom(rno=rno,des=des,ac=ac,roomtype=type,bedtype=bed,rate=rate,image=img)
       addRoom.save()
       messages.info(request, 'Room added successfully')
       return redirect('admin')
    return render(request, 'add_room.html')


def view_room(request):
    room = AddRoom.objects.all()
    context ={
        'room':room
    }

    return render(request,'view_room.html',context)


def view_customer(request):
    customer = CustomerDetails.objects.all()
    context ={
        'customer':customer
        }
    return render(request,'view_customer.html',context)

def update_room(request,id):
     room = AddRoom.objects.get(pk=id)
     if request.method=='GET':
        return render(request,'update_room.html',context={'room':room})  
   
     if request.method == 'POST':
       rno=request.POST['roomno']
       des=request.POST['des']
       ac=request.POST['ac']
       type=request.POST['type']

       bed=request.POST['bed']
       rate=request.POST['rate']
       img=request.FILES['img']
       room.rno = rno
       room.des = des
       room.ac = ac
       room.roomtype = type
       room.bedtype = bed
       room.rate = rate
       room.image = img
       room.save()

     return redirect('admin')
    

    


def delete_room(request,id):
    room = AddRoom.objects.get(pk=id)
    room.delete()
    return redirect('view_room')


def view_booking(request):
    booking = Book.objects.all()
    context ={
        'booking':booking
        }
    return render(request,'view_booking.html',context)

def delete_customer(request,id):
    customer = CustomerDetails.objects.get(pk=id)
    customer.delete()
    return redirect('view_customer')
 
def user_login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        uname = request.POST.get('uname')
        pswd = request.POST.get('pswd')
        user = authenticate(request, username=uname, password=pswd)
        if uname == 'admin' and pswd == 'admin':
            return redirect('admin')
        elif user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html')


def signup(request):
    if request.method=='GET':
        return render(request,'signup.html')
    elif request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        age=request.POST['age']
        adhar=request.POST['adhar']
        address=request.POST['address']
        email=request.POST['email']
        phnno=request.POST['mobileno']
        uname=request.POST['uname']
        pswd=request.POST['pswd']
        obj1=CustomerDetails(fname=fname,lname=lname,age=age,adhar=adhar,address=address,email=email,phnno=phnno)
        obj2=User(username=uname)
        obj2.set_password(pswd)
        obj2.save()
        obj1.user=obj2
        obj1.save()
        return redirect('login')
    


def logout_view(request):
	logout(request)
	return redirect('login')


        
def user_home(request):
    room = AddRoom.objects.all()
    context = {
        'room': room
    }
    return render(request, 'user_home.html', context)
def book(request, id):
    room = AddRoom.objects.get(id=id)
    if request.method == 'GET':
        return render(request, 'user_booking.html', context={'room': room})
    elif request.method == 'POST':
        checkin = request.POST['checkin']
        checkout = request.POST['checkout']
        obj1 = Book.objects.filter(checkin__gte=checkin, checkin__lte=checkout)
        obj2 = Book.objects.filter(checkout__gte=checkin, checkout__lte=checkout)
        if len(obj1) == 0 and len(obj2) == 0:
            a = datetime.strptime(checkin, "%Y-%m-%d").date()
            b = datetime.strptime(checkout, "%Y-%m-%d").date()
            no_of_days = (b - a).days
            total = no_of_days * room.rate
            return render(request, 'user_booking.html', context={'room': room, 'total': total, 'msg': "Available", 'checkin': checkin, 'checkout': checkout})
        else:
            return render(request, 'user_booking.html', context={'room': room, 'msg': "Not Available"})

def save_booking(request):
    if request.method=='POST':
        checkin=request.POST['chckin']
        checkout=request.POST['chckout']
        amount=request.POST['amount']
        roomid=request.POST['roomid']
        obj2=Book(checkin=checkin,checkout=checkout,amount=amount)
        customer=CustomerDetails.objects.get(user=request.user)
        room=AddRoom.objects.get(pk=roomid)
        obj2.customer=customer
        obj2.room=room
        obj2.save()
        return redirect('user_home')
    else:
        return redirect('user_home')

    
def view_userBooking(request):
    custmr=CustomerDetails.objects.get(user=request.user)
    booking = Book.objects.filter(customer=custmr)
    context = {
        'booking':booking
        }
    return render(request, 'view_user_booking.html', context)



def cancel_booking(request,id):
    booking = Book.objects.get(id=id)
    booking.delete()
    return redirect('view_user_booking')


def person_details(request):
    customer=CustomerDetails.objects.get(user=request.user)
    context = {
        'customer':customer
        }
    return render(request, 'person_details.html', context)


def update_details(request):
    customer = CustomerDetails.objects.get(user=request.user)
    if request.method == 'GET':
        return render(request, 'update_details.html', {'customer':customer})
    elif request.method=='POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        age=request.POST['age']
        adhar=request.POST['adhar']
        address=request.POST['address']
        email=request.POST['email']
        phnno=request.POST['mobileno']
        customer.fname=fname
        customer.lname=lname
        customer.age=age
        customer.adhar=adhar
        customer.address=address
        customer.email=email
        customer.phnno=phnno
        customer.save()
        return redirect('person_detail')
    











    
    







       
    



