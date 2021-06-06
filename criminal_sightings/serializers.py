from rest_framework import serializers
from criminal_sightings.models import CriminalSightingsAPI

class CriminalSightingsAPISerializer(serializers.ModelSerializer):

    class Meta:
        model = CriminalSightingsAPI
        fields = ('name','date','time','location','description')
 