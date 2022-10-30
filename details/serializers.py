from rest_framework import serializers

from .models import Details

class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=Details
        fields=[
            'slackUsername',
            'backend',
            'age',
            'bio',
        ]