from django.core.checks.messages import Error
from django.contrib.auth.hashers import check_password
from store.models.category import Category
from store.models.customer import Customer
from store.models import product
from django.shortcuts import render, redirect
from store.models import Product
from django.views import View


class Login(View):
    def get(self, request):
        return render(request, 'login.html')
    
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        validuser = Customer.get_customer_by_emailid(email)
        error_message = None
        if validuser:
            flag = check_password(password, validuser.password)
            if flag:
                request.session['user_id'] = validuser.id
                request.session['email'] = validuser.email
                return redirect('homepage')
            else:
                error_message = "Email or Password invalid!!"
        else:
            error_message = 'Email or Password Invalid!!'
        return render(request, 'login.html', {'error':error_message})

