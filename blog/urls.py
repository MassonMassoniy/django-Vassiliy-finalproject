from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
#from rest_framework.urlpatterns import format_suffix_patterns

router = DefaultRouter()
router.register('post', PostView, basename = 'post')

urlpatterns=[
    path('',index),
    path('about/',about),
    path('post/new/',post_form,name="post_form"),
    path('<int:pk>/',post_single,name='single'),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('api/', include(router.urls)),

    path('token/',TokenObtainPairView.as_view()),
    path('token/refresh/',TokenRefreshView.as_view()),

    path('register/',RegisterView.as_view({'post':'create'})),
    path('user/me/',UserView.as_view({'get':'get_current_user'})),

    path('courier/get/', CourierView.as_view()),
    path('seller/get/', SellerView.as_view()),
    path('assembler/get/', AssemblerView.as_view()),
    path('customer/get/', CustomerView.as_view()),
    path('administrator/get/', AdminView.as_view()),
]