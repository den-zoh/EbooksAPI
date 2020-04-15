from django.urls import path
from kitabu.api.views import EbookListCreateAPIView, EbookDetailAPIView, ReviewCreateAPIView, ReviewDetailAPIView

urlpatterns = [
    path("ebooks/", EbookListCreateAPIView.as_view(), name="book-list"),
    path("ebooks/<int:pk>/", EbookDetailAPIView.as_view(), name="book-detail"),
    path("ebooks/<int:ebook_pk>/review/", ReviewCreateAPIView.as_view(), name="review-list"),
    path("reviews/<int:pk>", ReviewDetailAPIView.as_view(), name="review-detail")
]
