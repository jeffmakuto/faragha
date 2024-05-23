from rest_framework_simplejwt.views import TokenObtainPairView
from serializers import CustomTokenObtainPairSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    """
    Custom token obtain pair view.
    """
    serializer_class = CustomTokenObtainPairSerializer