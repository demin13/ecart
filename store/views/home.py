from django.core.checks.messages import Error
from django.http.response import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from store.models.category import Category
from store.models.customer import Customer
from store.models import product
from django.shortcuts import redirect, render
from store.models import Product
from django.views import View

class Index(View):
    def get(self, request):
        product = None
        # request.session.get('cart').clear
        category = Category.get_all_category()
        categoryID = request.GET.get('category')
        if categoryID:
            product = Product.get_all_products_by_categoryid(categoryID)
        else:
            product = Product.get_all_products()
        dicts = {
            'products' : product,
            'categories' : category
        }
        print(request.session.get('email'))
        return render(request, 'index.html', dicts)
    
    def post(self, request):
        product = request.POST.get('product')
        cart = request.session.get('cart')
        if cart :
            quantity = cart.get(product)
            if quantity:
                cart[product] = quantity+1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        print(request.session['cart'])
        return redirect('homepage')