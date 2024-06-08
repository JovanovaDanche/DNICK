from django.shortcuts import render,redirect

# Create your views here.
from healthyFoodApp.models import Product
from healthyFoodApp.forms import ProductForm
def index(request):
    return render(request, 'index.html')


def outofstock(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            if not request.user.is_anonymous:
                form.instance.user=request.user
                form.save()
                return redirect('outofstock')
    else:
        form = ProductForm()

    products=Product.objects.filter(quantity__lt=1)
    return render(request,"outofstock.html",{"products":products,"form":form})