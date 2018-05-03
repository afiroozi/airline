from airline.form import AirCraftForm
from airline.models import Customer,Employee, Charter
from django.shortcuts import render
from django.db.models import Q



def customer_list(request):
    querylist = Customer.objects.all()

    context = {
        "custmer_list": querylist,
        "title": "Customer List"
    }
    return render(request, "airline/index.html", context)


def index(request):
    cus_list = Customer.objects.all()
    emp_list = Employee.objects.all()
    charter_list = Charter.objects.all()

    context = {
        "page_title": "Home Page",
        "cus_list": cus_list,
        "emp_list": emp_list,
        "charter_list": charter_list,
    }
    return render(request, "airline/index.html", context)


def addAircraft(request):
    form = AirCraftForm(request.POST or None)
    context = {
        "title": "Air Craft Form",
        "form": form
    }
    return render(request,"airline/addAircraft.html", context)


def report(request):
    # title 1
    cus_list = Customer.objects.filter(cus_areacode=615)

    # title 2
    cus_list2 = Customer.objects.filter(cus_areacode=615).filter(cus_balance__lte= 1000)

    # title 3
    chart_list3 = Charter.objects.filter(Q(cus_code=10011) | Q(cus_code=10014))

    # title 4
    chart_list4 = Charter.objects.filter(Q(cus_code=10011) | Q(cus_code=10014))

    context = {
        "title1": "List all customers who live in Area Code 615",
        "cus_list": cus_list,
        "title2": "List all customers who live in Area Code 615 and have a balance of less than $1000.00",
        "cus_list2": cus_list2,
        "title3": "List all charter trip information for Customer code 10011 and 10014.  ",
        "chart_list3": chart_list3,
        "title4": "List all charter trips information that has minimum of 1 hour and maximum of 5 hours waiting time.  ",
        "chart_list4": chart_list4,
    }
    return render(request, "airline/report.html", context)



