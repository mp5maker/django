from rest_framework.serializers import (
    ModelSerializer,
    Serializer
)

from .models import (
    Images,
    Description
)

class CommonSerializer(Serializer):

    class Meta:
        fields = (
            'name',
            'slug',
            'created',
            'updated'
        )


class ImagesSerializer(ModelSerializer):

    class Meta:
        model = Images
        fields = CommonSerializer.Meta.fields + (
            'image',
        )


class ImageDescriptionSerializer(ModelSerializer):
    images = ImagesSerializer()

    class Meta:
        model = Description
        fields = CommonSerializer.Meta.fields + (
            'description',
            'images'
        )

