from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet, AdminViewSet, ProductViewSet, CartViewSet, 
    OrderViewSet, OrderItemViewSet, ActionFigureViewSet, 
    BuildingToysViewSet, EducationalToysViewSet, 
    DollsAndStuffedAnimalsViewSet, GamesAndPuzzlesViewSet, 
    OutdoorToysViewSet, PretendPlayToysViewSet, 
    CreativeAndArtToysViewSet, ElectronicToysViewSet
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'admins', AdminViewSet)
router.register(r'products', ProductViewSet)
router.register(r'cart', CartViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'order-items', OrderItemViewSet)
router.register(r'Action-Figures', ActionFigureViewSet)
router.register(r'Building-Toys', BuildingToysViewSet)
router.register(r'Educational-Toys', EducationalToysViewSet)
router.register(r'Dolls-and-Stuffed-Animals', DollsAndStuffedAnimalsViewSet)
router.register(r'Games-and-Puzzles', GamesAndPuzzlesViewSet)
router.register(r'Outdoor-Toys', OutdoorToysViewSet)
router.register(r'Pretend-Play-Toys', PretendPlayToysViewSet)
router.register(r'Creative-and-Art-Toys', CreativeAndArtToysViewSet)
router.register(r'Electronic-Toys', ElectronicToysViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
