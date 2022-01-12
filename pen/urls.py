from django.urls import path
from pen import views

app_name = 'pen'

urlpatterns = [
    path('memo/', views.memo, name='memo')
]