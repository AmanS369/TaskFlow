

from rest_framework.permissions import IsAuthenticated
from tasks.models import Tasks, TaskGroup
from tasks.serializer import TaskSerializer, TaskGroupSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils.timezone import now
from datetime import date

class TaskGroupViewSet(viewsets.ModelViewSet):
    serializer_class = TaskGroupSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return TaskGroup.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['get'])
    def tasks(self, request, pk=None):
        group = self.get_object()
        tasks = Tasks.objects.filter(group=group)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def group_stats(self, request, pk=None):
        group = self.get_object()
        total_tasks = Tasks.objects.filter(group=group).count()
        completed_tasks = Tasks.objects.filter(group=group, is_complete=True).count()
        
        return Response({
            "group_name": group.name,
            "total_tasks": total_tasks,
            "completed_tasks": completed_tasks,
            "pending_tasks": total_tasks - completed_tasks
        })


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Tasks.objects.filter(user=self.request.user)
        group_id = self.request.query_params.get('group', None)
        if group_id:
            queryset = queryset.filter(group_id=group_id)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['get'])
    def stats(self, request):
        user_tasks = Tasks.objects.filter(user=request.user)
        total_tasks = user_tasks.count()
        total_done = user_tasks.filter(is_complete=True).count()
        total_pending = user_tasks.filter(is_complete=False).count()
        
        return Response({
            "total_tasks": total_tasks,
            "total_done": total_done,
            "total_pending": total_pending
        })
    
    @action(detail=False, methods=['get'])
    def due_today(self, request):
        today = date.today()
        tasks_due_today = Tasks.objects.filter(user=request.user, due_date=today,is_complete=False)
        serializer = self.get_serializer(tasks_due_today, many=True)
        return Response(serializer.data)