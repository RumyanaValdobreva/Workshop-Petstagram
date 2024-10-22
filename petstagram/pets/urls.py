from django.urls import path, include
from petstagram.pets import views


urlpatterns = [
    path('add/', views.add_pet_page, name='add-pet'),
    path('<str:username>/pet/<slug:pet_slug>/', include([
        path('', views.pet_details_page, name='pet-details'),
        path('edit/', views.edit_pet_page, name='edit_pet'),
        path('delete/', views.delete_pet_page, name='delete_pet'),
    ]))
]