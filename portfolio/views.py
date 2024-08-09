from django.shortcuts import render

from rest_framework import viewsets, generics
from .models import Category, Project, ProjectImage, ProjectVideo, Tag
from .serializers import CategorySerializer, ProjectSerializer, ProjectImageSerializer, ProjectVideoSerializer, \
    TagSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectImageViewSet(viewsets.ModelViewSet):
    queryset = ProjectImage.objects.all()
    serializer_class = ProjectImageSerializer


class ProjectVideoViewSet(viewsets.ModelViewSet):
    queryset = ProjectVideo.objects.all()
    serializer_class = ProjectVideoSerializer


class ProjectVideosList(generics.ListAPIView):
    serializer_class = ProjectVideoSerializer

    def get_queryset(self):
        project_id = self.kwargs['project_id']
        return ProjectVideo.objects.filter(project_id=project_id)


class ProjectImageList(generics.ListAPIView):
    serializer_class = ProjectImageSerializer

    def get_queryset(self):
        project_id = self.kwargs['project_id']
        return ProjectImage.objects.filter(project_id=project_id)


class ProjectByCategory(generics.ListAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return Project.objects.filter(category_id=category_id)


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
