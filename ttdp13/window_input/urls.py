from  django.urls import path
from .views import *

urlpatterns = [
    path('', win_inp, name="win_inp"),
    path('list_input/', list_input, name="list_inp")
]



