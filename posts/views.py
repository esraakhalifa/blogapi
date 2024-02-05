from django.shortcuts import render

from rest_framework import generics, permissions

from .models import Post

from .serializers import PostSerialzer

from .permissions import IsAuthorOrReadOnly

class PostList(generics.ListCreateAPIView):

    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerialzer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerialzer
# Create your views here.
