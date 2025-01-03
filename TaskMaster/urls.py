from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tasks.views import TaskViewSet, TaskGroupViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from django.contrib import admin
from django.urls import path,include
router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')
router.register(r'task-groups', TaskGroupViewSet, basename='task_group')
urlpatterns = [
         path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('auth/',include('auth.urls')),
      path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
     
]