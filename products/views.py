# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import Productserializer
from products import serializers


@api_view(['GET'])
def products_list(request):

    products = Product.objects.all()

    serializer =Productserializer(products,many = True)

    return Response(serializer.data)
