from rest_framework.serializers import ModelSerializer
from kitabu.models import Review, Ebook


class ReviewSerializer(ModelSerializer):

    class Meta:
        model = Review
        fields = "__all__"


class EbookSerializer(ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Ebook
        fields = "__all__"

