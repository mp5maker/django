from django.shortcuts import render

from rest_framework.response import Response

from rest_framework.generics import (
    ListCreateAPIView
)

from .models import (
    Description,
    Images
)

from .serializers import (
    ImagesSerializer,
    ImageDescriptionSerializer
)


class DescriptionListCreateView(ListCreateAPIView):
    queryset = Description.objects.all()
    serializer_class = ImageDescriptionSerializer

    def post(self, request, *args, **kwargs):
        print(request.data)
        return Response()
