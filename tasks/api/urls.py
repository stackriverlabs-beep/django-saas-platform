from rest_framework.routers import DefaultRouter
from .views import TaskViewSet
from django.urls import path
from .views import health_check


router = DefaultRouter()
router.register(r'tasks', TaskViewSet)


urlpatterns = router.urls
urlpatterns += [
    path('health/', health_check),
]