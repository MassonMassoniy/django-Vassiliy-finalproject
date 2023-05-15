from django.urls import path, include
from .views import index, about, post_single, post_form, PostViewSet
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

router = DefaultRouter()
router.register('post', PostViewSet, basename = 'post')

urlpatterns=[
    path('',index),
    path('about/',about),
    path('post/new/',post_form,name="post_form"),
    path('<int:pk>/',post_single,name='single'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('api/', include(router.urls))
]