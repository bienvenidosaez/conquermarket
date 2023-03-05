from marketplace.buyers.models import Buyer
from rest_framework import routers, serializers, viewsets
from django_filters.rest_framework import DjangoFilterBackend


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
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['uuid', ]
