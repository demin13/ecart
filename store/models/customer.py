from django.db import models
from django.db.models.fields import CharField, EmailField

#class Customer(models.Model):
class Customer(models.Model):
    fname = CharField(max_length=100)
    sname = CharField(max_length=100, null=True)
    phone = CharField(max_length=10)
    email = EmailField()
    password = CharField(max_length=200)
    confirmpassword = CharField(max_length=200)

    def registered(self):   
        self.save()
    
    def emailcheck(self):
        if Customer.objects.filter(email = self.email):
            return True
        return False
    def mobilecheck(self):
        if Customer.objects.filter(phone = self.phone):
            return True
        return False

    @staticmethod
    def get_customer_by_emailid(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False