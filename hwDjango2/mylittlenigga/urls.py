from django.urls import path
from . import views

urlpatterns = [
    path('', views.AdList.as_view(), name='ad_list'),
    path('ad/<int:pk>', views.AdDetail.as_view(), name='ad_detail'),
    path('ad/create', views.AdCreate.as_view(), name='ad_create'),
    path('ad/<int:pk>/update', views.AdUpdate.as_view(), name='ad_update'),
    path('ad/<int:pk>/delete', views.AdDelete.as_view(), name='ad_delete'),
    path('ad/<int:pk>/comment', views.CommentCreate.as_view(), name='comment_create'),

    path('login/', views.UserLoginView.as_view(), name='user_login'),
    path('logout/', views.UserLogoutView.as_view(), name='user_logout'),
    path('register/', views.SignUpView.as_view(), name='user_register'),

    path('accept/<str:username>/', views.check)
]