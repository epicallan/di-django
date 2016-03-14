from rest_framework import viewsets
from .serializers import SpotlightSerializer, IndicatorsSerializer
from spotlight.models import Spotlight, Indicators


class SpotlightViewSet(viewsets.ModelViewSet):
    queryset = Spotlight.objects.all()
    serializer_class = SpotlightSerializer


class IndicatorsViewSet(viewsets.ModelViewSet):
    queryset = Indicators.objects.all()
    serializer_class = IndicatorsSerializer
