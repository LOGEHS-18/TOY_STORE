from rest_framework import viewsets
from .models import User, Admin, Product, Cart, Order, OrderItem
from .serializers import UserSerializer, AdminSerializer, ProductSerializer, CartSerializer, OrderSerializer, OrderItemSerializer
from .serializers import UserSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .models import ActionFigure
from .serializers import ActionFigureSerializer
from .models import BuildingToys, EducationalToys, DollsAndStuffedAnimals, GamesAndPuzzles, OutdoorToys, PretendPlayToys, CreativeAndArtToys, ElectronicToys
from .serializers import BuildingToysSerializer, EducationalToysSerializer, DollsAndStuffedAnimalsSerializer, GamesAndPuzzlesSerializer, OutdoorToysSerializer, PretendPlayToysSerializer, CreativeAndArtToysSerializer, ElectronicToysSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

class MyProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        content = {'message': 'This is a protected view!'}
        return Response(content)


class ActionFigureViewSet(viewsets.ModelViewSet):
    queryset = ActionFigure.objects.all()
    serializer_class = ActionFigureSerializer

class BuildingToysViewSet(viewsets.ModelViewSet):
    queryset = BuildingToys.objects.all()
    serializer_class = BuildingToysSerializer

class EducationalToysViewSet(viewsets.ModelViewSet):
    queryset = EducationalToys.objects.all()
    serializer_class = EducationalToysSerializer

class DollsAndStuffedAnimalsViewSet(viewsets.ModelViewSet):
    queryset = DollsAndStuffedAnimals.objects.all()
    serializer_class = DollsAndStuffedAnimalsSerializer

class GamesAndPuzzlesViewSet(viewsets.ModelViewSet):
    queryset = GamesAndPuzzles.objects.all()
    serializer_class = GamesAndPuzzlesSerializer

class OutdoorToysViewSet(viewsets.ModelViewSet):
    queryset = OutdoorToys.objects.all()
    serializer_class = OutdoorToysSerializer

class PretendPlayToysViewSet(viewsets.ModelViewSet):
    queryset = PretendPlayToys.objects.all()
    serializer_class = PretendPlayToysSerializer

class CreativeAndArtToysViewSet(viewsets.ModelViewSet):
    queryset = CreativeAndArtToys.objects.all()
    serializer_class = CreativeAndArtToysSerializer

class ElectronicToysViewSet(viewsets.ModelViewSet):
    queryset = ElectronicToys.objects.all()
    serializer_class = ElectronicToysSerializer
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # Create (Handled by default in ModelViewSet)
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    # Read (Handled by default in ModelViewSet)
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)

    def perform_update(self, serializer):
        # You can add any custom logic here before saving
        serializer.save()
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    # Delete (Handled by default in ModelViewSet)
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    
@action(detail=False, methods=['post', 'put'])
def login(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return Response({'error': 'Email and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'error': 'Invalid email or password'}, status=status.HTTP_400_BAD_REQUEST)

        if request.method == 'POST':
            # Authenticate the user
            if user.password == password:
                serializer = self.get_serializer(user)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid email or password'}, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'PUT':
            # Update the user's email or password
            new_email = request.data.get('new_email', user.email)
            new_password = request.data.get('new_password', user.password)

            # Update the user object
            user.email = new_email
            user.password = new_password
            user.save()

            # Serialize and return the updated user data
            serializer = self.get_serializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
