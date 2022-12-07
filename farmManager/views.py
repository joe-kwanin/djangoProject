from ast import Try
import imp
from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from base.models import User, product, categories
from .models import records
from base import urls


# Create your views here.

@login_required(login_url='login')  # user must login to access this page
def dash(request):  # dashboard function
    context = {}
    n_total = []
    n_eggs = []
    age =[]
    rec = records.objects.all()
    re = rec.values()
    for r in re:
        n_total.append(r['total_stock'])
        n_eggs.append(r['egg_production'])
        age.append(r['age'])

    # # getting all top products
    toppro = product.objects.filter(veterinary=User.objects.get(username=request.user.username)).filter(
        score__gte=3).order_by('-score')
    if len(toppro) > 0:
        context["toppro"] = toppro
        context["notnone"] = "notnone"
    else:
        context["none"] = "none"
        context["records"] = n_total
        context["n_eggs"] = n_eggs



        # getting all products
    allpro = product.objects.filter(veterinary=User.objects.get(username=request.user.username))
    context["allpro"] = allpro
    context["records"] = n_total
    context["n_eggs"] = n_eggs
    context["age"] = age

    return render(request, "dashboard.html", context)


@login_required(login_url='login')
def myproduct(request):
    # creating a contex
    context = {}

    # getting all products by logged in seller
    mypro = product.objects.filter(veterinary=User.objects.get(username=request.user.username))
    if len(mypro) > 0:
        context["mypro"] = mypro
        context["notnone"] = "notnone"
    else:
        context["none"] = "none"

    # if "edit" in request.GET:
    #     eid = request.GET["edit"]
    #     print("Edit was clicked "+ eid)

    if "del" in request.GET:
        delid = request.GET["del"]
        # deleting the product
        product.objects.filter(id=delid).delete()

        return redirect("../products/")

    return render(request, "myproducts.html", context)


@login_required(login_url='login')
def addproduct(request):
    # context
    context = {}
    # getting all categories
    allcat = categories.objects.all()
    context["allcat"] = allcat

    # checking if a product is submitted
    if request.method == "POST":
        # getting username of the seller
        user = User.objects.get(username=request.user.username)
        try:
            # getting user inputs from html form
            title = request.POST["title"]
            desc = request.POST["desc"]
            sku = request.POST["sku"]
            brand = request.POST["brand"]
            cat = request.POST["cat"]
            price = request.POST["price"]
            imag = request.FILES["img"]

            try:
                product.objects.create(  # creating the new product
                    seller=user,
                    title=title,
                    desc=desc,
                    sku=sku,
                    price=price,
                    cart_price=price,
                    brand=brand,
                    cat=cat,
                    image=imag,
                )

                return redirect("../products/")  # redirecting to products page
            except Exception as e:
                print(e)
        except Exception as e:
            print(e)

    return render(request, "addproduct.html", context)


def edit(request, pid):
    context = {}

    # getting all categories
    allcat = categories.objects.all()
    context["allcat"] = allcat

    # getting the product with id
    theproduct = product.objects.get(id=pid)
    if theproduct is not None:
        context["pro"] = theproduct
    else:
        print("Did not get the product")

    # if user clicks on update button
    if request.method == "POST":
        # getting input from html form
        title = request.POST["title"]
        desc = request.POST["desc"]
        sku = request.POST["sku"]
        brand = request.POST["brand"]
        price = request.POST["price"]
        cat = request.POST["cat"]

        # updating product
        theproduct.title = title
        theproduct.desc = desc
        theproduct.sku = sku
        theproduct.brand = brand
        theproduct.price = price
        theproduct.cat = cat

        theproduct.save()  # saving product

        return redirect("../../products/")  # redirecting to products page

    return render(request, "editproduct.html", context)


@login_required(login_url='login')
def recordsGet(request):
    if request.method == 'POST':
        print(request.POST)
        pen = request.POST['pen']
        production = request.POST['pro']
        age = request.POST['age']
        birds = request.POST['birds']
        feed = request.POST['feed']
        egg = request.POST['egg']
        stock = request.POST['stock']
        medication = request.POST['med']
        remarks = request.POST['remarks']

        rec = records()
        rec.pen_no = pen
        rec.save()
        rec.production_type = production
        rec.save()
        rec.age = int(age)
        rec.save()
        rec.no_birds = int(birds)
        rec.save()
        rec.feed = int(feed)
        rec.save()
        rec.egg_production = int(egg)
        rec.save()
        rec.total_stock = int(stock)
        rec.save()
        rec.medication = medication
        rec.save()
        rec.remarks = remarks
        rec.save()
    return render(request, "records.html")

@login_required(login_url='login')
def chart(request):
    context={}
    rec = records.objects.all()
    re = rec.values()
    date = []
    production_ = []
    age = []
    n_birds = []
    feed = []
    n_eggs = []
    n_total = []

    for r in re:
        date.append(r['date_received'].strftime('%x'))
        production_.append(r['production_type'])
        age.append(r['age'])
        n_birds.append(r['no_birds'])
        feed.append(r['feed'])
        n_eggs.append(r['egg_production'])
        n_total.append(r['total_stock'])
        print(date)

    context = {'date': date, 'production_type': production_, 'age': age, 'no_birds': n_birds, 'feed': feed, 'no_eggs': n_eggs, 'total_stock': n_total}
    return render(request, "charts.html", context)


@login_required(login_url='login')  # user must login to access this page
def logoutUser(request):  # logoutUser function
    logout(request)  # logout user
    return redirect("../../")  # got back to homepage
