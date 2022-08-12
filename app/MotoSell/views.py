from rest_framework.response import Response
from rest_framework import generics, permissions
from .serializers import OfferSerializer
from .models import Offer
# Create your views here.


class OfferListView(generics.ListCreateAPIView):
    """
    Get list of Offers.
    permissions - AllowAny
    """
    queryset = Offer.objects.all().filter(is_pub=True).order_by('-pub_date')
    serializer_class = OfferSerializer
    permission_classes = [permissions.AllowAny]
    name = 'offer-list'


class OfferDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Get details of Offer by it's id.
    Delete only by Offer.user
    permissions - isAuthenticatedOrReadOnly
    """
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    name = 'offer-detail'

    def destroy(self, request, *args, **kwargs):
        offer = self.get_object()
        offer.is_deleted = True
        offer.save()
        return Response(data='delete success')
