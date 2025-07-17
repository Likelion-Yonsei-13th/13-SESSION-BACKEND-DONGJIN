from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from django.urls import reverse

# 상품 등록
def product_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        Product.objects.create(name=name, description=description, price=price)
        return redirect('product_list')
    return render(request, 'shop/product_form.html')

# 전체 상품 조회
def product_list(request):
    products = Product.objects.all().order_by('-id')
    return render(request, 'shop/product_list.html', {'products': products})

# 개별 상품 조회
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'shop/product_detail.html', {'product': product})

# 상품 수정
def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.description = request.POST.get('description')
        product.price = request.POST.get('price')
        product.save()
        return redirect('product_detail', pk=product.pk)
    return render(request, 'shop/product_form.html', {'product': product, 'edit': True})

# 상품 삭제
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'shop/product_confirm_delete.html', {'product': product})
