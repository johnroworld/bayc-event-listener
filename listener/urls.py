from django.urls import path
from listener import views

urlpatterns = [
    path('transfer-history/<int:token_id>/', views.get_transfer_history, name='transfer_history'),
]