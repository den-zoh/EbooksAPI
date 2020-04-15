from rest_framework import generics
from rest_framework import mixins
from kitabu.models import Ebook, Review
from kitabu.api.serializers import EbookSerializer


class EbookListCreateAPIView(mixins.ListModelMixin,mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer

    def get(self,request, *args, **kwargs):
        return self.list(self, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(self, *args, **kwargs)
