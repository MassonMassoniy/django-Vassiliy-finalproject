from django.urls import path
from .views import index, about, post_single, post_form

urlpatterns=[
    path('',index),
    path('about/',about),
    path('post/new/',post_form,name="post_form"),
    path('<int:pk>/',post_single,name='single')
]