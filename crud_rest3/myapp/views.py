from rest_framework import viewsets
from myapp.models import ItemModel, UserModel
# Create your views here.
from myapp.serializers import UserSerializers, ItemSerializers



class UserViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializers
    
    
class ItemViewSet(viewsets.ModelViewSet):
    queryset = ItemModel.objects.all()
    serializer_class = ItemSerializers