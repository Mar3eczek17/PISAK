from django.urls import path
from pen import views

app_name = 'pen'

urlpatterns = [
    path('memo/', views.memo, name='memo'),
    path('add_new_memo/', views.add_new_memo, name='add_new_memo'),
    path('show_all_memos/', views.show_all_memos, name='show_all_memos'),
]