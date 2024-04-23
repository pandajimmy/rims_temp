from .models import TtaListCalLogs
from rest_framework import serializers


class TtaListCalLogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TtaListCalLogs
 #      depth = 1
        fields = '__all__'