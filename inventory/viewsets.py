from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('-created_at')
    serializer_class = ProductSerializer
    
    @action(detail=False, methods=['get'])
    def search(self, request):
        """Search products by name or SKU"""
        query = request.query_params.get('q', '')
        products = Product.objects.filter(
            name__icontains=query
        ) | Product.objects.filter(sku__icontains=query)
        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)
