from rest_framework import serializers
from tasks.models import Tasks, TaskGroup

class TaskGroupSerializer(serializers.ModelSerializer):
    total_tasks = serializers.SerializerMethodField()
    completed_tasks = serializers.SerializerMethodField()
   

    class Meta:
        model = TaskGroup
        fields = ['id', 'name', 'description', 'created_at', 'updated_at', 
                 'total_tasks', 'completed_tasks']
        
    def get_total_tasks(self, obj):
        return obj.tasks.count()
    
    def get_completed_tasks(self, obj):
        return obj.tasks.filter(is_complete=True).count()
    
    

class TaskSerializer(serializers.ModelSerializer):
    group_name = serializers.CharField(source='group.name', read_only=True)
    
    class Meta:
        model = Tasks
        fields = ['id', 'title', 'description', 'is_complete', 'created_at', 
                 'updated_at', 'due_date','priority', 'group', 'group_name']
        read_only_fields = ['id', 'created_at', 'updated_at']