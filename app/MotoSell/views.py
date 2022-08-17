from rest_framework.response import Response
from rest_framework import generics, permissions
from .serializers import OfferSerializer
from .models import Offer
from .permissions import IsOfferOwner
# Create your views here.


class OfferListView(generics.ListCreateAPIView):
    """
    Get list of Offers.
    permissions - AllowAny
    """
    queryset = Offer.objects.all().filter(is_pub=True).order_by('-pub_date')
    serializer_class = OfferSerializer
    permission_classes = [permissions.AllowAny]
    authentication_classes = []
    name = 'offer-list'


class OfferDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Get details of Offer by it's id.
    Delete only by Offer.user
    permissions - isAuthenticatedOrReadOnly
    """
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    permission_classes = [permissions.IsAuthenticated]
    name = 'offer-detail'

    def destroy(self, request, *args, **kwargs):
        offer = self.get_object()
        offer.is_deleted = True
        offer.save()
        return Response(data='delete success')


class UserOfferListView(generics.ListCreateAPIView):
    """
    Get list of Offers added by authorized user.
    permissions - IsAuthenticated
    """
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    permission_classes = [permissions.IsAuthenticated, IsOfferOwner]
    name = 'user-offers'

    def get_queryset(self):
        offers = Offer.objects.filter(user=self.request.user.id, is_deleted=False).order_by('-pub_date')
        return offers


class UserOfferDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Get details of Offer by it's id.
    Delete only by Offer.user by setting flag is_deleted to true
    permissions - isAuthenticatedOrReadOnly, IsOfferOwner
    """
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOfferOwner]
    name = 'user-offer-detail'

    def destroy(self, request, *args, **kwargs):
        offer = self.get_object()
        if offer.user == self.request.user:
            offer.is_deleted = True
            offer.save()
        return Response(data='delete successfully')
