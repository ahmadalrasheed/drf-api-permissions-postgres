from rest_framework import generics
from .models import application
from .serializer import applicationSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsAuthorOrReadOnly


class applicationListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = application.objects.all()
    serializer_class = applicationSerializer


class applicationDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = application.objects.all()
    serializer_class = applicationSerializer