from django.urls import path, include
from . import views


urlpatterns = [
    path('offers', views.OfferListView.as_view(), name=views.OfferListView.name),
    path('offers/<int:pk>', views.OfferDetail.as_view(), name=views.OfferDetail.name),
]
