from rest_framework import serializers
from criminal_data.models import CriminalDataAPI

class CriminalDataAPISerializer(serializers.ModelSerializer):

    class Meta:
        model = CriminalDataAPI
        fields = ('name','dob','known_crimes','registered','registered_at','custody','latest_sightings_time','latest_sightings_date','latest_sightings_place')
 