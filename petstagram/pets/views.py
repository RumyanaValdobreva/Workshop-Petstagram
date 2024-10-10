from django.shortcuts import render


def add_pet_page(request):
    return render(request, 'pets/pet-add-page.html')


def delete_pet_page(request, username, pet_slug):
    return render(request, 'pets/pet-delete-page.html')


def details_pet_page(request, username, pet_slug):
    return render(request, 'pets/pet-details-page.html')


def edit_pet_page(request, username, pet_slug):
    return render(request, 'pets/pet-edit-page.html')