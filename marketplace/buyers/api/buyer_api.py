from marketplace.buyers.models import Buyer
from rest_framework import routers, serializers, viewsets


class BuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyer
        fields = [
            'uuid',
            'coins',
            'products',
        ]


class BuyerViewSet(viewsets.ModelViewSet):
    queryset = Buyer.objects.all()
    serializer_class = BuyerSerializer
