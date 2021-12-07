from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, status, filters

from . import serializers, models

User = get_user_model()


class EventsView(generics.ListAPIView):
    queryset = models.Event.objects.all()
    serializer_class = serializers.EventsListOutputSerializer
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        return self.queryset.filter(Q(created_by=self.request.user) \
            | Q(guests__in=[self.request.user,]))


class EventsGetView(APIView):

    def get(self, request, pk):
        obj = get_object_or_404(models.Event, pk=pk, created_by=self.request.user)
        return Response(serializers.EventsGetOutputSerializer(obj).data)


class EventsCreateView(APIView):

    def post(self, request):
        serializer = serializers.EventsCreateSerializer(data=request.data)
        # DIY, try to create a validations
        serializer.is_valid(raise_exception=True)
        obj = serializer.save()
        return Response(serializers.EventsGetOutputSerializer(obj).data)


class EventsUpdateView(APIView):

    def put(self, request, pk):
        obj = get_object_or_404(models.Event, pk=pk, created_by=self.request.user)
        serializer = serializers.EventsCreateSerializer(obj, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        obj = serializer.save()
        return Response(serializers.EventsGetOutputSerializer(obj).data)


class EventsDeleteView(APIView):

    def delete(self, request, pk):
        obj = get_object_or_404(models.Event, pk=pk, created_by=self.request.user)
        obj.delete()
        return Response({'success':True})