from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),

  path('creds/', views.creds_index, name='index'),
  path('creds/<int:cred_id>/', views.creds_detail, name='detail'),
  path('creds/create/', views.CredCreate.as_view(), name='creds_create'),
  path('creds/<int:pk>/update/', views.CredUpdate.as_view(), name='creds_update'),
  path('creds/<int:pk>/delete/', views.CredDelete.as_view(), name='creds_delete'),

  path('urls/', views.URLList.as_view(), name='urls_index'),
  path('urls/<int:pk>/', views.URLDetail.as_view(), name='urls_detail'),
  path('urls/create/', views.URLCreate.as_view(), name='urls_create'),
  path('urls/<int:pk>/update/', views.URLUpdate.as_view(), name='urls_update'),
  path('urls/<int:pk>/delete/', views.URLDelete.as_view(), name='urls_delete'),

  path('cats/<int:cred_id>/add_URL_to_Cred/<int:url_id>/', views.add_URL_to_Cred, name='addUrlToCred'),
  path('cats/<int:cred_id>/remove_URL_to_Cred/<int:url_id>/', views.remove_URL_to_Cred, name='removeUrlToCred'),
]