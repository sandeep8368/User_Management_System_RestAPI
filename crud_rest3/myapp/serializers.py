from rest_framework import serializers
from myapp.models import UserModel, ItemModel

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'
        
        
        
class ItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = ItemModel
        fields = '__all__'