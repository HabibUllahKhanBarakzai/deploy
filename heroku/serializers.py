from rest_framework.serializers import ModelSerializer
from .models import HerokuModel


class HerokuSerializers(ModelSerializer):
    class Meta:
        model = HerokuModel
        fields = "__all__"
