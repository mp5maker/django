from django.shortcuts import render, get_object_or_404

from cart.forms import CartAddProductForm

from .models import (
    Category,
    Product
)

def product_list(request, *args, **kwargs):
    category = None
    products = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
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
    print(id)
    print(slug)
    product = get_object_or_404(Product, id=id, slug=slug)
    cart_product_form = CartAddProductForm()
    return render(
        request,
        'shop/product/detail.html',
        {
            "product": product,
            'cart_product_form': cart_product_form
        },
    )