from django.urls import path
from. import views


urlpatterns=[
    path("",views.Tax,name="tax"),
    path("<int:number>",views.calculate,name="calculate"),
    path("taxrate",views.dispaly,name="taxrate")
]