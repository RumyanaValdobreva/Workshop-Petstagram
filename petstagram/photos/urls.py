from django.urls import path, include
from petstagram.photos import views


urlpatterns = [
    path('photos/', views.PhotoAddPage.as_view(), name='add-photo'),
    path('<int:pk>/', include([
        path('', views.PhotoDetailsPage.as_view(), name='photo-details'),
        path('edit/', views.PhotoEditPage.as_view(), name='photo_edit'),
        path('delete/', views.photo_delete, name='photo_delete'),
    ])),
]