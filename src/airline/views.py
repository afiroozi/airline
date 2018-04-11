from airline.models import Customer
from django.shortcuts import render


def customer_list(request):
    querylist = Customer.objects.all()
    context = {
        "custmer_list": querylist
    }
    return render(request, "airline/index.html", context)



