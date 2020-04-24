from django.urls import path, include

from . import views

urlpatterns = [
    path('categories', views.ViewCategories.as_view(), name='get-categories'),
    path('coupons/<int:id>/', views.ViewCoupons.as_view(), name='get-coupons'),
    # path('coupons', views.ViewCoupons.as_view(), name='get-coupons'),

]
