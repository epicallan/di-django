'''
serializer classes for the DI admin models
'''
from rest_framework import serializers
from spotlight.models import Spotlight, Indicators


class SpotlightSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = Spotlight


class IndicatorsSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = Indicators
