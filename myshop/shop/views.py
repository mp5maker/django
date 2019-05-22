from django.shortcuts import render

from .models import (
    Category,
    Product
)

def product_list(request, *args, **kwargs):
    category = None
    products = None
    categories = Category.objects.all()
    product = Product.objects.filter(available=True)
    category_slug = kwargs.get('category_slug')
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(
        request,
        'shop/product/list.html',
        {
            "category": category,
            "products": products,
            "categories": categories
        }
    )

def product_detail(request, *args, **kwargs):
    id = kwargs.get('id')
    slug = kwargs.get('slug')
    product = get_object_or_404(Product, id=id, slug=slug)
    return render(
        request,
        'shop/product/details.html',
        {"product": product}
    )