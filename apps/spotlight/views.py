from rest_framework import viewsets
from .serializers import SpotlightSerializer, IndicatorSerializer
from spotlight.models import Spotlight, Indicator
from rest_framework.parsers import FileUploadParser


class SpotlightViewSet(viewsets.ModelViewSet):
    queryset = Spotlight.objects.all()
    serializer_class = SpotlightSerializer
    lookup_field = 'slug'


class IndicatorViewSet(viewsets.ModelViewSet):
    queryset = Indicator.objects.all()
    serializer_class = IndicatorSerializer
    parser_classes = (FileUploadParser,)
    lookup_field = 'slug'
    
    def pre_save(self, obj):
        obj.upload = self.request.FILES.get('file')
        # lets do what we what with our file upload
        # like process and pass it to an api to save it a database
