from django.shortcuts import render

from rest_framework.response import Response

from rest_framework.parsers import MultiPartParser

from rest_framework.generics import (
    ListCreateAPIView
)

from .models import (
    Description,
    Images
)

from .serializers import (
    ImagesSerializer,
    DescriptionSerializer
)

class DescriptionListCreateView(ListCreateAPIView):
    queryset = Description.objects.all()
    serializer_class = DescriptionSerializer
    parser_classes = (MultiPartParser, )

    def post(self, request, *args, **kwargs):
        image_description = Description.objects.create(
            name=request.POST.get('name'),
            description=request.POST.get('description')
        )
        for image in request.FILES.getlist('images'):
            Images.objects.create(
                image=image,
                name=request.POST.get('name'),
                description=Description.objects.get(pk=1)
            )

        return Response()