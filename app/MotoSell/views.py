from rest_framework.mixins import UpdateModelMixin
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework import generics, permissions, status
from .serializers import OfferSerializer
from .models import Offer
from .permissions import IsOfferOwner
# Create your views here.


class OfferListView(generics.ListCreateAPIView):
    """
    Get list of Offers.
    permissions - IsAuthenticatedOrReadOnly
    """
    queryset = Offer.objects.all().filter(is_pub=True, is_deleted=False).order_by('-pub_date')
    serializer_class = OfferSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    name = 'offer-list'
    parser_classes = [FormParser, MultiPartParser]


    def post(self, request):
        context = {'request': request}
        reg_serializer = OfferSerializer(data=request.data, context=context)
        if reg_serializer.is_valid():
            new_offer = reg_serializer.save()
            if new_offer:
                return Response(status=status.HTTP_201_CREATED)
        return Response(reg_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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


class UserOfferListView(generics.ListCreateAPIView):
    """
    Get list of Offers added by authorized user.
    permissions - IsAuthenticated
    """
    # queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    permission_classes = [permissions.IsAuthenticated, IsOfferOwner]
    name = 'user-offers'

    def get_queryset(self):
        offers = Offer.objects.filter(user=self.request.user, is_deleted=False).order_by('-pub_date')
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

    def perform_destroy(self, instance):
        if self.request.user == instance.user:
            instance.is_deleted = True
            instance.is_pub = False
        instance.save()

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class OfferPublishView(generics.RetrieveUpdateDestroyAPIView, UpdateModelMixin):
    """
    You just need to provide the field which is to be modified.
    """
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    name = 'offer-publish-view'

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
