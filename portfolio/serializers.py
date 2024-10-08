from rest_framework import serializers
from .models import Category, Project, ProjectImage, ProjectVideo, Tag
import cloudinary


class CategorySerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'title', 'image', 'image_url']

    def get_image_url(self, obj):
        return obj.image.url


# class ProjectSerializer(serializers.ModelSerializer):
#     image_url = serializers.SerializerMethodField()
#
#     class Meta:
#         model = Project
#         fields = '__all__'
#
#     def get_image_url(self, obj):
#         return obj.url.url


class ProjectImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = ProjectImage
        fields = ['id', 'project', 'image', 'image_url']  # List all fields explicitly

    def get_image_url(self, obj):
        return obj.image.url


class ProjectVideoSerializer(serializers.ModelSerializer):
    video_url = serializers.SerializerMethodField()

    class Meta:
        model = ProjectVideo
        fields = ['id', 'project', 'video', 'video_url']  # List all fields explicitly

    def get_video_url(self, obj):
        return obj.video.url


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name', 'type', 'height', 'width']


class ProjectSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    tags = TagSerializer(many=True, read_only=True)
    images = ProjectImageSerializer(many=True, read_only=True)
    videos = ProjectVideoSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ['name', 'description', 'tags', 'images', 'videos','url']

    def get_url(self, obj):
        return obj.url.url
