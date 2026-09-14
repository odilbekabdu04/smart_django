from django.urls import path
from . import views

urlpatterns = [
    # Auth
    path('register/', views.register_view, name='api_register'),
    path('login/', views.login_view, name='api_login'),
    path('admin-login/', views.admin_login_view, name='api_admin_login'),
    path('me/', views.me_view, name='api_me'),

    # Stats
    path('stats/', views.stats_view, name='api_stats'),

    # Users
    path('users/', views.users_view, name='api_users'),
    path('users/<int:user_id>/', views.user_detail_view, name='api_user_detail'),
    path('users/<int:user_id>/block/', views.toggle_block_view, name='api_toggle_block'),

    # Products (Mahsulotlar)
    path('rest/', views.RestListCreateView.as_view(), name='api_rest_list'),
    path('rest/<int:pk>/', views.RestDetailView.as_view(), name='api_rest_detail'),
]