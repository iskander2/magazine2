from itertools import product
from django.shortcuts import render
from .models import Category,Category2
from .forms import Category2Form

# Create your views here.
def shop(request):
    form = Category2Form(request.POST,request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
    products = Category2.objects.all()
    categories = Category.objects.all()    
    return render (request,'shop.html',{'products':products, 'categories':categories,'form':form  })

def ololo(request):
    form = Category2Form(request.POST or None)
    category = Category2.objects.all()
    if request.method == 'POST' and form.is_valid():
        form.save()
    return render (request,'shop.html',{'form':form })

            

