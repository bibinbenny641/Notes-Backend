from django.urls import path
from . import views

urlpatterns = [
    path('addnotes/',views.Notes_view.as_view(),name='addnote'),
    path('addnotes/<id>/',views.Notes_view.as_view(),name='addnote2'),
]