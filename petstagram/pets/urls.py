from django.urls import path, include
from petstagram.pets import views


urlpatterns = [
    path('add/', views.add_pet_page, name='add_pet'),
    path('<str:username>/pet/<slug:pet_slug>/', include([
        path('', views.details_pet_page, name='details_pet'),
        path('edit/', views.edit_pet_page, name='edit_pet'),
        path('delete/', views.delete_pet_page, name='delete_pet'),
    ]))
]