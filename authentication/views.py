from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from geeksforgeeks import settings
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth import authenticate, login, logout
from . tokens import generate_token
import gradcap_final
import txt_to_pdf


# Create your views here.
def home(request):
    if request.method == "POST":
        fileName = request.FILES["file"]
        print(fileName)
        return render(request,"")
    return render(request, "authentication/index.html")

def contract_upload(request):
    return render(request,"authentication/contract_upload.html")

def dashboard(request):
    return render(request,'authentication/dashboard.html')


def pricing(request):
    return render(request,"authentication/pricing.html")


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        if User.objects.filter(username=username):
            messages.success(request, "Username already exist! Please try some other username.")
            return redirect('signup')
        
        if User.objects.filter(email=email).exists():
            messages.success(request, "Email Already Registered!!")
            return redirect('signup')
        
        if len(username)>20:
            messages.success(request, "Username must be under 20 charcters!!")
            return redirect('signup')
        
        if pass1 != pass2:
            messages.success(request, "Passwords didn't matched!!")
            return redirect('signup')
        
        if not username.isalnum():
            messages.success(request, "Username must be Alpha-Numeric!!")
            return redirect('signup')
        
        myuser = User.objects.create_user(username, email, pass1)
        # myuser.first_name = fname
        # myuser.last_name = lname
        # # myuser.is_active = False
        myuser.save()
        messages.success(request, "Your Account has been created succesfully!! Log in to use our services.")
        
        # Welcome Email
        # subject = "Welcome to GFG- Django Login!!"
        # message = "Hello " + myuser.first_name + "!! \n" + "Welcome to GFG!! \nThank you for visiting our website\n. We have also sent you a confirmation email, please confirm your email address. \n\nThanking You\nAnubhav Madhav"        
        # from_email = settings.EMAIL_HOST_USER
        # to_list = [myuser.email]
        # send_mail(subject, message, from_email, to_list, fail_silently=True)
        
        # Email Address Confirmation Email
        # current_site = get_current_site(request)
        # email_subject = "Confirm your Email @ GFG - Django Login!!"
        # message2 = render_to_string('email_confirmation.html',{
            
        #     'name': myuser.first_name,
        #     'domain': current_site.domain,
        #     'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
        #     'token': generate_token.make_token(myuser)
        # })
        # email = EmailMessage(
        # email_subject,
        # message2,
        # settings.EMAIL_HOST_USER,
        # [myuser.email],
        # )
        # email.fail_silently = True
        # email.send()
        
        return redirect('signin')
        
        
    return render(request, "authentication/signup.html")



def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        print(username)
        print(pass1)
        user = authenticate(username=username, password=pass1)
        if user is not None:
            login(request, user)
            fname = user.username
            messages.success(request, "Logged In Sucessfully!!")
            return redirect("dashboard")
        else:
            messages.success(request, "Bad Credentials!!")
            return render(request, "authentication/signin.html")
    
    
    return render(request, "authentication/signin.html")


def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('home')

def formContract(request):
    if request.method == "POST":
        name = request.POST["name"]
        parents_name = request.POST["parents_name"]
        aadhar_no = request.POST["Aadhar"]
        gstin = request.POST["GSTIN"]
        iex = request.POST["IEX"]
        category = request.POST["category"]
        purpose = request.POST["purpose"]
        acceptance = request.POST["acceptance"]
        StartDate = request.POST["StartDate"]
        EndDate = request.POST["EndDate"]
        Amount = request.POST["Amount"]
        location = request.POST["location"]
        
        if(aadhar_no!="" and gstin=="" and iex==""):
            asa = txt_to_pdf.createPdf(gradcap_final.org(acceptance),gradcap_final.name(name),gradcap_final.name(parents_name),22,purpose,gradcap_final.date(StartDate),gradcap_final.date(EndDate),gradcap_final.location(location),gradcap_final.name(acceptance))
        if(aadhar_no=="" and gstin!="" and iex==""):
            asa = txt_to_pdf.createPdf(gradcap_final.org(acceptance),gradcap_final.name(name),gradcap_final.name(parents_name),22,purpose,gradcap_final.date(StartDate),gradcap_final.date(EndDate),gradcap_final.location(location),gradcap_final.name(acceptance))
        if(aadhar_no=="" and gstin=="" and iex!=""):
            asa = txt_to_pdf.createPdf(gradcap_final.org(acceptance),gradcap_final.name(name),gradcap_final.name(parents_name),22,purpose,gradcap_final.date(StartDate),gradcap_final.date(EndDate),gradcap_final.location(location),gradcap_final.name(acceptance))
        
        if(asa):
            return redirect('dashboard')
        else:
            return redirect('home')
    return render(request,"authentication/form1.html")