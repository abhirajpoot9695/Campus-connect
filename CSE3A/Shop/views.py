from django.shortcuts import render,HttpResponse

from .models import Contact # type: ignore

# Create your views here.
def index(request):
    return render (request,"Index.HTML")

# def welcome_page(request):
#     return render(request, 'Welcome.HTML') # File ka naam wahi rakhein jo aapne rakha hai
def home(request):
    return render (request,"home.HTML")

def about(request):
    return render (request,"about.HTML")

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")

        phone = request.POST.get("phone")

        msg = request.POST.get("msg")
        
        c = Contact(name=name,email=email,phone=phone,msg=msg)
        c.save()
    data = Contact.objects.all()    
    return render (request,'contact.HTML',{"data":data})


def login(request):
    return render (request,"login.html")


def signup(request):
    return render (request,"signup.html")

def features(request):
    return render (request,"features.HTML")

