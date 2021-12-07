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
    permission_classes = [IsAuthenticated,]

    def get(self, request, pk):
        obj = get_object_or_404(models.Event, pk=pk, created_by=self.request.user)
        return Response(serializers.EventsGetOutputSerializer(obj).data)


class EventsCreateView(APIView):
    permission_classes = [IsAuthenticated,]

    def post(self, request):
        serializer = serializers.EventsCreateSerializer(data=request.data)
        # DIY, try to create a validations
        serializer.is_valid(raise_exception=True)
        obj = serializer.save()

        # create invite
        for g in obj.guests.all(): models.Invite.objects.create(event=obj,to_user=g)

        return Response(serializers.EventsGetOutputSerializer(obj).data)


class EventsUpdateView(APIView):
    permission_classes = [IsAuthenticated,]

    def put(self, request, pk):
        obj = get_object_or_404(models.Event, pk=pk, created_by=self.request.user)
        serializer = serializers.EventsCreateSerializer(obj, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        obj = serializer.save()

        # create invite
        for g in obj.guests.all(): models.Invite.objects.create(event=obj,to_user=g)

        return Response(serializers.EventsGetOutputSerializer(obj).data)


class EventsDeleteView(APIView):
    permission_classes = [IsAuthenticated,]

    def delete(self, request, pk):
        obj = get_object_or_404(models.Event, pk=pk, created_by=self.request.user)
        obj.delete()
        return Response({'success':True})


class InvitesView(generics.ListAPIView):
    queryset = models.Invite.objects.all()
    serializer_class = serializers.InvitesListOutputSerializer
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        return self.queryset.filter(to_user=self.request.user)


class InvitesAcceptView(APIView):

    def post(self, request, pk):
        obj = get_object_or_404(models.Invite, pk=pk, to_user=self.request.user)
        if obj.status != models.Invite.STATUS_PENDING:
            return Response({'message': 'Already accepted or denied'})
        obj.status = models.Invite.STATUS_ACCEPTED
        obj.save()
        return Response(serializers.InvitesListOutputSerializer(obj).data)


class InvitesDenyView(APIView):

    def post(self, request, pk):
        obj = get_object_or_404(models.Invite, pk=pk, to_user=self.request.user)
        if obj.status != models.Invite.STATUS_PENDING:
            return Response({'message': 'Already accepted or denied'})
        obj.status = models.Invite.STATUS_DENIED
        obj.save()
        return Response(serializers.InvitesListOutputSerializer(obj).data)