# myapp/urls.py

from django.urls import path
from .views import sse_view
from django.views.generic import TemplateView

urlpatterns = [
    path('sse/', sse_view, name='sse'),
    path('sse-client/', TemplateView.as_view(template_name='sse_client.html'), name='sse_client'),
]
