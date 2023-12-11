"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from users.views import register, profile, logout_view
from blog.views import PostListView, PostDetailView, PostCreateView, PostUpdateView, AboutView, PostDeleteView
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('about/', AboutView.as_view(), name='blog-about'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('logout/', logout_view, name='logout'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
