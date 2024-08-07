from django.db import models
from cloudinary.models import CloudinaryField

class Category(models.Model):
    title = models.CharField(max_length=255)
    image = CloudinaryField('image')

    def __str__(self):
        return self.title

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, related_name='projects', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image = CloudinaryField('image')

    def __str__(self):
        return f"Image for {self.project.name}"

class ProjectVideo(models.Model):
    project = models.ForeignKey(Project, related_name='videos', on_delete=models.CASCADE)
    video = CloudinaryField('video',resource_type='video')

    def __str__(self):
        return f"Video for {self.project.name}"
