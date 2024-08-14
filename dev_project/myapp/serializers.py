from rest_framework import serializers
from .models import User, Admin, Product, Cart, Order, OrderItem,ActionFigure, BuildingToys, EducationalToys, DollsAndStuffedAnimals, GamesAndPuzzles, OutdoorToys, PretendPlayToys, CreativeAndArtToys, ElectronicToys


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class BuildingToysSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuildingToys
        fields = '__all__'

class EducationalToysSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationalToys
        fields = '__all__'

class DollsAndStuffedAnimalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DollsAndStuffedAnimals
        fields = '__all__'

class GamesAndPuzzlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GamesAndPuzzles
        fields = '__all__'

class OutdoorToysSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutdoorToys
        fields = '__all__'

class PretendPlayToysSerializer(serializers.ModelSerializer):
    class Meta:
        model = PretendPlayToys
        fields = '__all__'

class CreativeAndArtToysSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreativeAndArtToys
        fields = '__all__'

class ElectronicToysSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectronicToys
        fields = '__all__'
class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    items = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'
        
class ActionFigureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActionFigure
        fields = ['id', 'name', 'category', 'subcategory', 'company', 'price', 'image']