from rest_framework import viewsets
from tasks.models import Task
from tasks.api.serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-created_at')
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    

    def get_queryset(self):
        return Task.objects.filter(
            owner=self.request.user
        ).order_by('-created_at')
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def health_check(request):
    return Response({"status": "ok"})