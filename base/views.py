from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def home(request):
    return render(request, 'base/main.html')


def loginPage(request):
    if request.user.is_authenticated:
        if request.user.atype == "veterinary":
            return redirect("veterinary_dash/")
        else:
            return redirect("../farmManager_dash/")

    if request.method == "POST":
        try:
            email = request.POST["email"]
            passs = request.POST["password"]
            print(passs)

            auth = authenticate(request, username=email, password=passs)
            if auth is not None:
                login(request, auth)
                if request.user.atype == "veterinary":
                    return redirect("../veterinary_dash/")
                else:
                    return redirect("../farmManager_dash/")
            else:
                print("Error loggin in")
        except Exception as e:
            print(e)

    #
    # if request.method == 'POST':
    #     email = request.POST.get('email')
    #     password = request.POST.get('password')
    #
    #     try:
    #         user = User.objects.get(email=email)
    #     except:
    #         messages.error(request, 'User does not exist')
    #     user = authenticate(request, email=email, password=password)
    #
    #     if user is not None:
    #         login(request, user)
    #         return redirect('home')
    #     else:
    #         messages.error(request, 'Username or password is incorrect')
    context = {}
    return render(request, 'base/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    if request.method == "POST":
        try:
            name = request.POST["name"]
            business = request.POST["business"]
            type = request.POST["type"]
            email = request.POST["email"]
            password = request.POST["password"]
            cpassword = request.POST["rpassword"]
            location = request.POST["location"]
            contact = request.POST["contact"]

            if password == cpassword:
                user = User()
                user.username = email
                user.save()
                user.email = email
                user.save()
                user.name = name
                user.save()
                user.atype = type
                user.save()
                user.set_password(cpassword)
                user.save()
                user.business_name = business
                user.save()
                user.location = location
                user.save()
                user.contact = contact
                user.save()

                # loggin user in after a successful registration
                auth = authenticate(request, username=email, password=cpassword)
                if auth is not None:
                    login(request, auth)
                    if request.user.atype == "veterinary":
                        return redirect("../veterinary_dash/")
                    elif request.user.atype == "farm manager":
                        return redirect("../farmManager_dash/")
                else:
                    print("Error logging in")

        except Exception as e:
            print(e)

        return redirect("../")
    else:
        pass
    return render(request, 'base/register.html')