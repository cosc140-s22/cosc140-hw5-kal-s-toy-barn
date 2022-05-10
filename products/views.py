from django.shortcuts import render, get_object_or_404
from django.db.models import Prefetch
from .models import Product, ProductImage
from .forms import ProductFilterForm

def index(request):
    parameters = request.GET
    products = Product.objects.all().order_by('name')
    form = ProductFilterForm(request.GET)
    name_search = request.GET.get('name_search')
    min_price_search = request.GET.get('min_price')
    max_price_search = request.GET.get('max_price')
  
    if name_search:
        products = products.filter(name__icontains=name_search)
    
    if min_price_search:
      products = products.filter(price__gte=min_price_search)

    if max_price_search:
      products = products.filter(price__lte=max_price_search)
      
    if parameters.get("sort") == 'age':
      products = Product.objects.all().order_by('minimum_age_appropriate')
    if parameters.get("sort") == 'price':
      products = Product.objects.all().order_by('price')
      
    context = {'products': products, 'form': form}
    return render(request, 'products/index.html', context)

def show(request, product_id):
    p = get_object_or_404(Product, pk=product_id)
    i = p.productimage_set.all()
    context = { 'product':p, 'images':i if i.exists() else None}
    return render(request, 'products/show.html', context)
    
