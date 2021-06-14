from django.http import HttpResponse
from rest_framework.decorators import api_view


@api_view(['GET'])
def get_index(request):
    if request.method == 'GET':
        return HttpResponse(content='Cards API')
