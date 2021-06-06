from rest_framework.decorators import api_view
from alerts.serializers import AlertAPISerializer as TutorialSerializer
from alerts.models import AlertAPI as Tutorial
from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from datetime import date
today = date.today()
today = today.strftime("%Y-%m-%d")


@api_view(['GET', 'POST', 'DELETE'])
def alerts(request):
    if request.method == 'GET':
        tutorials = Tutorial.objects.all()

        title = request.query_params.get('name', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)

        tutorials_serializer = TutorialSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = TutorialSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Tutorial.objects.all().delete()
        return JsonResponse({'message': '{} Alerts were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'DELETE'])
def alert_name(request, name):
    # tutorials = Tutorial.objects.filter(title=title)
    tutorials = Tutorial.objects.filter(
        name=name)
    if request.method == 'GET':
        tutorials_serializer = TutorialSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)

    elif request.method == 'DELETE':
        tutorials.delete()
        return JsonResponse({'message': 'Alert was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'DELETE'])
def alert_subject(request, subject):
    # tutorials = Tutorial.objects.filter(title=title)
    tutorials = Tutorial.objects.filter(
        subject=subject)
    if request.method == 'GET':
        tutorials_serializer = TutorialSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)

    elif request.method == 'DELETE':
        tutorials.delete()
        return JsonResponse({'message': 'Alert was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
