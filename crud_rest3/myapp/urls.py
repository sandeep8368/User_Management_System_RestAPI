from django.urls import path,include
from rest_framework.routers import DefaultRouter
from myapp.views import UserViewSet, ItemViewSet


router = DefaultRouter()

router.register(r'users',UserViewSet)
router.register(r'items',ItemViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
