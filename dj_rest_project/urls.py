"""
URL configuration for dj_rest_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from product.views import ProductAPIView, CommentViewSet, RatingViewSet, ProductDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/product/', ProductAPIView.as_view(), name='product'),
    path('api/comment/', CommentViewSet.as_view({'get': 'list'}), name='comment'),
    path('api/rating/', RatingViewSet.as_view({'get': 'list'}), name='rating'),
    path('api/prdetail/', ProductDetailView.as_view())
]
