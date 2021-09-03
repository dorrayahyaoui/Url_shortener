from rest_framework.serializers import ModelSerializer
from .. import models


class Url_serviceSerializer(ModelSerializer):
    class Meta:
        model = models.Url_service
        fields = '__all__'
