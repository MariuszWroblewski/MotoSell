from rest_framework import permissions


class IsOfferOwner(permissions.BasePermission):
    """
    Offer owner permission.
    """

    def has_object_permission(self, request, view, obj):  # noqa: D102
        return request.user == obj.user
