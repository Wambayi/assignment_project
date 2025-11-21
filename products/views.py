from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from .models import Product

# Form to add products
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'price', 'description', 'image']

# View to add a product
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_products')
    else:
        form = ProductForm()
    return render(request, 'products/add_product.html', {'form': form})

# View to list all products
def list_products(request):
    products = Product.objects.all()
    return render(request, 'products/list_products.html', {'products': products})

#   product detail page
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_detail.html', {'product': product})
