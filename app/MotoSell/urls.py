from django.urls import path, include
from . import views


urlpatterns = [
    path('offers', views.OfferListView.as_view(), name=views.OfferListView.name),
    path('offers/<int:pk>', views.OfferDetail.as_view(), name=views.OfferDetail.name),
    path('offers/my-offers', views.UserOfferListView.as_view(), name=views.UserOfferListView.name),
    path('offers/my-offers/<int:pk>', views.UserOfferDetail.as_view(), name=views.UserOfferDetail.name),
    path('offers/my-offers/publish/<int:pk>', views.OfferPublishView.as_view(), name=views.OfferPublishView.name),
]
