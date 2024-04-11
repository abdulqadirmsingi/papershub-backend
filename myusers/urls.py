from django.urls import path
from .views import CustomTokenObtainPairView
from rest_framework_simplejwt import views as jwt_views
from .views import ActivateUser

urlpatterns = [
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('refresh/', jwt_views.TokenRefreshView.as_view(), name='refresh'),
    path('activation/<str:uid>/<str:token>', ActivateUser.as_view({'get': 'activation'}), name='activation'),
]

# urlpatterns = [
#     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


#     path('register', views.RegisterUserGet.as_view({'get': 'list'}), name= 'registeruser'),
#     path('res/', views.RegisterUserPost.as_view(), name= 'res'),
#     # path('login', views.LoginView.as_view(), name= 'login'),
# ]