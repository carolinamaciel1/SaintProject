from rest_framework import serializers
from saints.models import Saints


class SaintsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'name',
            'country',
            'description'
        )

        model = Saints
