from django.urls import path

from . import views

urlpatterns = [
    path('events/', views.EventsView.as_view(), name='events'),
    path('events/create/', views.EventsCreateView.as_view(), name='events-create'),
    path('events/get/<str:pk>/', views.EventsGetView.as_view(), name='events-get'),
    path('events/update/<str:pk>/', views.EventsUpdateView.as_view(), name='events-update'),
    path('events/delete/<str:pk>/', views.EventsDeleteView.as_view(), name='events-delete'),

    #
    path('invites/accept/<str:pk>/', views.InvitesAcceptView.as_view(), name='invites-accept'),
    path('invites/deny/<str:pk>/', views.InvitesDenyView.as_view(), name='invites-deny'),
    path('invites/', views.InvitesView.as_view(), name='invites'),
]