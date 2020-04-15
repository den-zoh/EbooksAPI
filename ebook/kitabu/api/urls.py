from django.urls import path
from kitabu.api.views import EbookListCreateAPIView

urlpatterns = [
    path("ebooks/", EbookListCreateAPIView.as_view(), name="book-list")
]