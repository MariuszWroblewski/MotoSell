from rest_framework.response import Response
from .models import Offer
from rest_framework import generics, permissions
from .serializers import OfferSerializer
# Create your views here.


class OfferListView(generics.ListCreateAPIView):
    """
    Get list of Offers.
    """
    queryset = Offer.objects.all().order_by('-pub_date')
    serializer_class = OfferSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    name = 'offer-list'


class OfferDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Get details of Offer by it's id.
    """
    queryset = Offer.objects.all().order_by('-pub_date')
    serializer_class = OfferSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    name = 'offer-detail'

    def destroy(self, request, *args, **kwargs):
        offer = self.get_object()
        offer.is_deleted = True
        offer.save()
        return Response(data='delete seccess')
