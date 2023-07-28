from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'newsletters', views.NewsletterViewSet, basename='newsletter')
router.register(r'articles', views.ArticleViewSet, basename='article')
router.register(r'users', views.UserViewSet, basename='user')

urlpatterns = [
    path('register/', views.user_registration, name='user-registration'),
    path('users/<int:pk>/', views.UserViewSet, name='user-detail'),
]

urlpatterns += router.urls
