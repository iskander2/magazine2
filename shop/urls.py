from django.urls import path
from .views import shop,ololo

app_name="shop"

urlpatterns = [
    path('',shop, name="shop"),
    path('1/',ololo, name="ololo"),

]    