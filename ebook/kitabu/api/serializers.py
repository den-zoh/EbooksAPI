from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from kitabu.models import Review, Ebook


class ReviewSerializer(ModelSerializer):
    review_author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        exclude = ("ebook",)
        # fields = "__all__"


class EbookSerializer(ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Ebook
        fields = "__all__"

