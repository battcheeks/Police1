from rest_framework import serializers
from alerts.models import AlertAPI

class AlertAPISerializer(serializers.ModelSerializer):

    class Meta:
        model = AlertAPI
        fields = ('name','date','time','subject','link')
 