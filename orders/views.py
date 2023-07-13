from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from .import serializers
from.models import Order
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth import get_user_model



User = get_user_model()


class HelloOrdeView(generics.GenericAPIView):

    @swagger_auto_schema(operation_summary="Hello Order")
    def get(self, request):
        return Response(data={"message":"Hello Order"}, status=status.HTTP_200_OK)


class OrderCreateListView(generics.GenericAPIView):

    serializer_class = serializers.OrderCreationSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]   
    queryset = Order.objects.all()

    @swagger_auto_schema(operation_summary="List of  all Orders")
    def get(self,request):
        orders=Order.objects.all()

        serializer=self.serializer_class(instance=orders,many=True)

        return Response(data=serializer.data,status=status.HTTP_200_OK)

    # def get(self,request):

    #     orders = Order.objects.all()
        
        
    #     serializer = self.serializer_class(instance=orders, many=True)
    #     return Response(data=serializer.data, status=status.HTTP_200_OK)


    @swagger_auto_schema(operation_summary="Create a new Order")
    def post(self, request):
        data = request.data

        serializer = self.serializer_class(data=data,)

        user = request.user

        if serializer.is_valid():
            serializer.save(customer=user)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        pass

class OrderDetailView(generics.GenericAPIView):
    serializer_class =serializers.OrderDetailSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_summary="Getting an  Order")
    def get(self, request, order_id):

        order = get_object_or_404(Order, pk=order_id)
        serializer = self.serializer_class(instance=order)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
        
    @swagger_auto_schema(operation_summary="Updating an order")
    def put(self, request, order_id):

        order=get_object_or_404(Order,pk=order_id)
        
        serializer=self.serializer_class(instance=order,data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data,status=status.HTTP_200_OK)

        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(operation_summary="Deleting an Order")
    def delete(self, request, order_id):

        order=get_object_or_404(Order,pk=order_id)

        order.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

class UpdateorderStatus(generics.GenericAPIView):

    serializer_class = serializers.OrderStatusUpdateSerializer
    permission_classes = [IsAuthenticated]
    
    @swagger_auto_schema(operation_summary="Updating an Order Status")
    def put(self,request, order_id):

        order=get_object_or_404(Order,pk=order_id)

        data = request.data

        serializer = self.serializer_class(data=data, instance=order)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserOrdersView(generics.GenericAPIView):

    serializer_class = serializers.OrderDetailSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]

    @swagger_auto_schema(operation_summary="Getting a User's order Order")
    def get(self, request, user_id):

        user = User.objects.get(pk=user_id)

        orders = Order.objects.all().filter(customer=user)

        serializer = self.serializer_class(instance=orders, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class UserOrderDetailView(generics.GenericAPIView):
    serializer_class=serializers.OrderDetailSerializer
    permission_classes=[IsAdminUser]


    @swagger_auto_schema(operation_summary="Getting all User's Orders")
    def get(self,request,user_id,order_id):
        user=User.objects.get(pk=user_id)

        order=Order.objects.all().filter(customer=user).get(pk=order_id)


        serializer=self.serializer_class(instance=order)

        return Response(data=serializer.data,status=status.HTTP_200_OK)

    
    







# Create your views here.
