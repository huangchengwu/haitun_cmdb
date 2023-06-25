from rest_framework.serializers import ModelSerializer
from .models import *
 
class clusterSerializer(ModelSerializer):
    class Meta:
        model = cluster
        fields = '__all__'

