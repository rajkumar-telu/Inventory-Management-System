from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product
# Create your views here. handling user reqs & rendering responses

#Home View
def home_view(request):
    return render(request,'imsApp/home.html')

#Create View
def product_create_view(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    return render(request,'imsApp/product_form.html',{'form':form})

#Read View
def product_list_view(request):
    products = Product.objects.all()
    return render(request, 'imsApp/product_list.html',{'products':products})

#Update View
def product_update_view(request,product_id):
    product = Product.objects.get(product_id=product_id)

    form = ProductForm(instance=product)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    return render(request, 'imsApp/product_form.html', {'form': form})

#Delete View
def product_delete_view(request,product_id):
    product = Product.objects.get(product_id=product_id)
    
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request,'imsApp/product_delete_confirm.html',{'product':product})


