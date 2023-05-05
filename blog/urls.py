from django.urls import path
from .views import index, about, post_single

urlpatterns=[
    path('',index),
    path('about/',about),
    path('<int:pk>/',post_single,name='single')
]