from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProjectViewSet, ProjectImageViewSet, ProjectVideoViewSet, ProjectVideosList, \
    ProjectImageList

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'project-images', ProjectImageViewSet)
router.register(r'project-videos', ProjectVideoViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('project/<int:project_id>/videos/', ProjectVideosList.as_view(), name='project-videos-list'),
    path('project/<int:project_id>/images/', ProjectImageList.as_view(), name='project-videos-image'),

]
