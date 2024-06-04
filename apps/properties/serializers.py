from django_countries.serializer_fields import CountryField
from django_countries.serializers import CountryFieldMixin
from rest_framework import serializers
from .models import Property, PropertyPhoto, PropertyViews


class PropertyPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyPhoto
        fields = ["photo"]


class PropertySerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    country = CountryField(name_only=True)
    property_photos = PropertyPhotoSerializer(many=True, read_only=True, source="property_photo")

    class Meta:
        model = Property
        fields = "__all__"

    def get_user(self, obj):
        return obj.user.username


class PropertyCreateSerializer(serializers.ModelSerializer):
    country = CountryField(name_only=True)
    property_photos = PropertyPhotoSerializer(many=True, read_only=True, source="property_photo")

    class Meta:
        model = Property
        exclude = ["updated_at", "pkid"]

    # def create(self, validated_data):
    #     property_photos_data = validated_data.pop("property_photos")
    #     property_instance = Property.objects.create(**validated_data)

    #     for photo_data in property_photos_data:
    #         PropertyPhoto.objects.create(property=property_instance, **photo_data)

    #     return property_instance


class PropertyViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyViews
        exclude = ["updated_at", "pkid"]
