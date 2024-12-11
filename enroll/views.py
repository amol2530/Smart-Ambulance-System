from encodings import CodecRegistryError
from multiprocessing import context
from urllib import request
from django.http import  JsonResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import CompanyForm,postForm
from enroll.models import newuser , Contact, Hospital,Bookambulance,Hospitaldetails,Area,Ambulance
# from .forms import Companyreg
# import swal from sweetalert
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


from django.contrib.auth import authenticate

# Create your views here.


def navbar(request):
    return render(request, 'base.html')

def home(request):

    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def help(request):
    return render(request, 'help.html')
def contact(request):
    return render(request, 'contact.html')

def user_login(request):
  
        if request.method== 'POST':
            try:
                Userdetailes=newuser.objects.get(Username=request.POST['Username'], pass1=request.POST['pass1'])
                print("Username=",Userdetailes)
                request.session['Username']=Userdetailes.Username
                messages.success(request,"successfully login")
                return redirect('user_home')
            except newuser.DoesNotExist as e:   
                messages.error(request,"Username/ Password Invalied...!")
        return render(request, 'user_login.html')
   

def user_registration(request):
    if request.method == 'POST':
        Username=request.POST['Username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        if pass1 !=pass2:
            messages.error(request,"password do not match")
            return redirect('user_registration')
        newuser(Username=Username, fname=fname, lname=lname, email=email, pass1=pass1, pass2=pass2).save()
        messages.success(request, 'The new user '+request.POST['Username']+ " IS saved successfully..!")
        return redirect('user_login')
    else:
        return render(request, 'user_registration.html')
    
def user_logout(request):
    # logout(request)
    messages.success(request,"successfully logout..!")
    return redirect('home')

# user changepassword

def user_changepassword(request):
    return render(request, 'user_changepassword.html')

def user_home(request):
    return render(request, 'user_home.html')

def user_contact(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        desc=request.POST['desc']
        contacts= Contact(name=name,email=email,phone=phone,desc=desc)
        contacts.save()    
        return redirect('user_contact')
    else:
        return render(request, 'user_contact.html')

def user_searchambulance(request):
    return render (request, 'user_searchambulance.html')

def search(request):
    query=request.GET['query']
    form=Hospitaldetails.objects.filter(haddress__icontains=query)
    return render (request, 'search.html',{'forms':form})

def map(request):
    # form=Bookambulance.objects.all()
    form = Bookambulance.objects.latest('id')

    return render(request,'map.html',{'form':form})


def ambulance(request):
    form = Ambulance.objects.all()
    return render(request,'ambulance.html',{'forms':form})


def ambulance_update(request, id):
    # if request.user.is_authenticated:
        if request.method =='POST':
            pi=Ambulance.objects.get(pk=id)
            fm = postForm(request.POST,instance=pi)
            if fm.is_valid():
                fm.save()
                return redirect('ambulance')  
        else:
            pi=Ambulance.objects.get(pk=id)
            fm = postForm(instance=pi)
        return render(request,'ambulance_update.html', {'form':fm })
        
        # return redirect('hospital')

    



def user_bookambulance(request,id):
  
    if request.method =='POST':
        pi=Hospitaldetails.objects.get(pk=id)
        fm = CompanyForm(request.POST,instance=pi)
        print(request)
        if fm.is_valid():
            fname=request.POST['fname']
            lname=request.POST['lname']
            hname=request.POST['hname']
            address=request.POST['address']
            uphone=request.POST['uphone']
            
            age=request.POST['age']
            gender=request.POST['gender']
            fm=Bookambulance(fname=fname, lname=lname,hname=hname, address=address, uphone=uphone,age=age,gender=gender)
            fm.save()
            return redirect("map") 
    else:
        pi=Hospitaldetails.objects.get(pk=id)
        fm = CompanyForm(instance=pi)
        
    return render(request,'user_bookambulance.html', {'form':fm })
   

# def user_bookambulance(request):
#     if request.method == 'POST':
#         fname=request.POST['fname']
#         lname=request.POST['lname']
       
#         address=request.POST['address']
#         uphone=request.POST['uphone']
#         tambulance=request.POST['tambulance']
#         age=request.POST['age']
#         gender=request.POST['gender']
#         Bookambulance(fname=fname, lname=lname, address=address, uphone=uphone, tambulance=tambulance,age=age,gender=gender).save()
#         # messages.success(request, 'The new user '+request.POST['Username']+ " IS saved successfully..!")
#         return redirect('map')
#     else:
#         return render(request, 'user_bookambulance.html')






    
def admin_registration(request):
    if request.method == 'POST':
        Username=request.POST['Username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        if pass1 !=pass2:
            messages.error(request,"password do not match")
            return redirect('user_registration')
        newuser(Username=Username, fname=fname, lname=lname, email=email, pass1=pass1, pass2=pass2).save()
        messages.success(request, 'The new user '+request.POST['Username']+ " IS saved successfully..!")
        return redirect('admin_login')
    else:
        return render(request, 'admin_registration.html')


def admin_login(request):
    if request.method== 'POST':
        try:
            Userdetailes=newuser.objects.get(Username=request.POST['Username'], pass1=request.POST['pass1'])
            print("Username=",Userdetailes)
            request.session['Username']=Userdetailes.Username
            messages.success(request,"successfully login")
            return redirect('admin_home')
        except newuser.DoesNotExist as e:   
            messages.error(request,"Username/ Password Invalied...!")
    return render(request, 'admin_login.html')

def admin_home(request):
    return render(request, 'admin_home.html')

def admin_contact(request):
    form=Contact.objects.all()
    return render(request, 'admin_contact.html', {'forms':form})



def admin_logout(request):
    messages.success(request,"successfully logout..!")
    return redirect('home')

def view_user(request):
    form=newuser.objects.all()
    return render(request,'view_user.html' , {'forms':form})

def hospital_ambulance(request):
    if request.method=='POST':
        hname=request.POST['hname']
        address=request.POST['address']
        area=request.POST['area']
        ambno=request.POST['ambno']
        dname=request.POST['dname']
        phone=request.POST['phone']
        hospital= Hospital(hname=hname,address=address,ambno=ambno,dname= dname, phone=phone,area=area)
        hospital.save()    
        return redirect('hospital_ambulance')
    else:
        return render(request, 'hospital_ambulance.html')

def views_booking_detailes(request):
    # user = request.user
    form = Bookambulance.objects.all()
    return render (request, 'views_booking_detailes.html', {'forms': form})

def ambulance_type(request):
    return render(request, 'ambulance_type.html')


def admin_about(request):
    return render(request, 'admin_about.html')



def hospital(request):
    
    return render(request, 'hospital.html')


def hospital_login (request):
    if request.method== 'POST':
            try:
                Userdetailes=Hospitaldetails.objects.get(hemail=request.POST['hemail'], pass1=request.POST['pass1'])
                print("hemail=",Userdetailes)
                request.session['hemail']=Userdetailes.hemail
                messages.success(request,"successfully login")
                return redirect('hospital')
            except Hospitaldetails.DoesNotExist as e:   
                messages.error(request,"Email/ Password Invalied...!")
    return render(request, 'hospital_login.html')

def hospital_registration (request):
    if request.method == 'POST':
        hname=request.POST['hname']
        htype=request.POST['htype']
        haddress=request.POST['haddress']
        hcontact=request.POST['hcontact']
        hemail=request.POST['hemail']
        ambno=request.POST['ambno']
        dname=request.POST['dname']
        dphone=request.POST['dphone']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']     
        Hospitaldetails(hname=hname,htype=htype,haddress=haddress,hcontact=hcontact, hemail=hemail,ambno=ambno,dname=dname,dphone=dphone, pass1=pass1, pass2=pass2).save()
        messages.success(request, 'The new user '+request.POST['hemail']+ " IS saved successfully..!")
        return redirect('hospital_login')
    else:
        return render(request, 'hospital_registration.html')


# Shortest path dijkstra algo 
import heapq

def dijkstra(graph, start, end):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    path = {}

    while pq:
        (curr_dist, curr_node) = heapq.heappop(pq)

        if curr_node == end:
            shortest_path = []
            while curr_node != start:
                shortest_path.append(curr_node)
                curr_node = path[curr_node]
            shortest_path.append(start)
            shortest_path.reverse()
            return shortest_path

        if curr_dist > distances[curr_node]:
            continue

        for neighbor, dist in graph[curr_node].items():
            distance = curr_dist + dist
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
                path[neighbor] = curr_node

    return None
# @login_required(login_url='hospital_login')








def check_patient(request):
    return render(request,'check_patient.html')





def index(request):
    return render (request,'index.html')    




