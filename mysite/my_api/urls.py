from . import views
from rest_framework import routers
from my_api.viewsets import TaskViewSet

app_name = 'my_api'
router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)