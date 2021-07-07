from django.contrib import admin
from django.urls import path
from store.views.home import Index
from store.views.login import Login
from store.views.signup import Signup


urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('signup', Signup.as_view()),
    path('login', Login.as_view())
]
