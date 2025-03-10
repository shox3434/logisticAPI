from django.urls import path
from .views import RegisterView, LoginView, DriverProfileView, CargoListCreateView, CargoDetailView, CargoReviewCreateView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', DriverProfileView.as_view(), name='profile'),
    path('cargos/', CargoListCreateView.as_view(), name='cargo-list-create'),
    path('cargos/<int:pk>/', CargoDetailView.as_view(), name='cargo-detail'),
    path('reviews/', CargoReviewCreateView.as_view(), name='review-create'),
]