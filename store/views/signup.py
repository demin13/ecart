from django.contrib.auth.hashers import make_password
from store.models.category import Category
from store.models.customer import Customer
from store.models import product
from django.shortcuts import render, redirect
from store.models import Product
from django.views import View

class Signup(View):
    def validataCustomer(self, customerdata):
        error_message = None
        if customerdata.emailcheck():
            error_message = "Email Already registered"
        elif customerdata.mobilecheck():
            error_message = "Mobile Number Already Registered"
        elif not customerdata.fname:
            error_message = "first name is required"
        elif not customerdata.sname:
            error_message = "second name is required"
        elif not customerdata.phone:
            error_message = "phone number is required"
        elif len(customerdata.phone) < 10:
            error_message = "Phone Number Length is below 10 digit"
        elif len(customerdata.phone) > 10:
            error_message = "Phone Number Length is above 10 digit"
        elif not customerdata.password :
            error_message = "Please Enter Password"
        elif not customerdata.confirmpassword :
            error_message = "Please Enter confirm Password"
        elif customerdata.password != customerdata.confirmpassword:
            error_message = "passwords donot match"
        return error_message
    def registerUser(self, request):
        postData = request.POST
        f_name = postData.get('fname')
        s_name = postData.get('sname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        Confirmpassword = postData.get('confirmpassword')
        customvalues = {'fname' : f_name,
            'sname' : s_name,
            'phone' : phone,
            'email' : email,
        }
        customerdata = Customer(fname = f_name,
            sname = s_name,
            phone = phone,
            email = email,
            password = password,
            confirmpassword = Confirmpassword
        )
        error_message = self.validataCustomer(customerdata)
        if(error_message is None):
            customerdata.password = make_password(customerdata.password)
            customerdata.confirmpassword = make_password(customerdata.confirmpassword)
            customerdata.registered()
            return redirect('homepage')
        else:
            data = {
                'error' : error_message,
                'filledvalues' : customvalues
            }
            return render(request, 'signup.html', data)
    def get(self, request):
        return render(request, 'signup.html')
    def post(self, request):
        return self.registerUser(request)