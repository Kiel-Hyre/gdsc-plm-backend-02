from api.accounts.serializers import AccountsUserSerializer
from rest_framework import exceptions, serializers

from . import models



class EventsListOutputSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Event
        fields = ['id',
        'title', 'date_start', 'date_end', 'time_start', 'time_end',
        'created_at', 'created_by', 'updated_at',]


class EventsGetOutputSerializer(EventsListOutputSerializer):
    guests = AccountsUserSerializer(many=True)
    invites = serializers.SerializerMethodField()

    class Meta:
        model = models.Event
        fields = EventsListOutputSerializer.Meta.fields + ['description', 'guests', 'invites',]

    def get_invites(self, obj):
        return InvitesWithoutEventSerializer(
                models.Invite.objects.filter(event=obj), many=True
            ).data


class EventsCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Event
        exclude = ['id', 'created_at', 'updated_at',]


class InvitesWithoutEventSerializer(serializers.ModelSerializer):
    to_user = AccountsUserSerializer()

    class Meta:
        model = models.Invite
        fields = ['id', 'to_user', 'status', 'created_at', 'updated_at',]


class InvitesListOutputSerializer(serializers.ModelSerializer):
    event = EventsGetOutputSerializer()

    class Meta:
        model = models.Invite
        fields = '__all__'


class DeleteYASG(serializers.Serializer):
    success = serializers.BooleanField()