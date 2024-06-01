from django.http import StreamingHttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import MyModel
from .serializers import MyModelSerializer
import time
import json


@api_view(['GET'])
def sse_view(request):
    def event_stream():
        while True:
            time.sleep(1)
            new_data = MyModel.objects.all()
            serializer = MyModelSerializer(new_data, many=True)
            json_data = json.dumps(serializer.data)
            yield f'data: {json_data}\n\n'

    response = StreamingHttpResponse(event_stream(), content_type='text/event-stream')
    response['Cache-Control'] = 'no-cache'
    return response
