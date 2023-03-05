from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import routers, serializers, viewsets
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import pagination
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


from django.http import Http404

from marketplace.buyers.models import Buyer
from marketplace.products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'pk',
            'name',
            'description',
            'image',
            'price',
            'purchased',
            'image_url'
        ]

    def get_image_url(self, product):
        if product.image:
            return f'http://conquermarket.34018.net:8000/media/{product.image}'
        return ''


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(purchased=False)
    serializer_class = ProductSerializer


# class MyProductsViewSet(generics.ListAPIView):
#     serializer_class = ProductSerializer

#     def get_queryset(self):
#         buyer_uuid = self.kwargs['buyer_uuid']
#         buyer = Buyer.objects.get(uuid=buyer_uuid)
#         return buyer.products.all()


class MyProductsViewSet(APIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request, buyer_uuid, format=None):
        if not Buyer.objects.filter(uuid=buyer_uuid).exists():
            raise Http404()

        buyer = Buyer.objects.get(uuid=buyer_uuid)
        data = {'count': buyer.products.count(), 'products': []}

        for product in buyer.products.all():
            product_data = ProductSerializer(product)
            product_data = product_data.data
            product_data['image'] = f'http://localhost:8000{product_data["image"]}'
            data['products'].append(product_data)

        return Response(data)

    def post(self, request, buyer_uuid, format=None):
        if not Buyer.objects.filter(uuid=buyer_uuid).exists():
            raise Http404()

        buyer = Buyer.objects.get(uuid=buyer_uuid)
        product = Product.objects.get(pk=request.data['product_pk'])

        product.purchased = True
        product.save()
        buyer.products.add(product)
        buyer.coins = buyer.coins - product.price
        buyer.save()
        return Response(status=201)


class CreateProductView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        products_serializer = ProductSerializer(data=request.data)
        if products_serializer.is_valid():
            products_serializer.save()
            return Response(products_serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', products_serializer.errors)
            return Response(products_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Reset(APIView):

    def get(self, request, format=None):
        Buyer.objects.all().delete()
        Product.objects.all().update(purchased=False)
        return Response(status=201)
