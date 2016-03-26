'''
serializer classes for the DI admin models
'''
from rest_framework import serializers
from spotlight.models import Spotlight, Indicator


class SpotlightSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = Spotlight


class IndicatorSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = Indicator
