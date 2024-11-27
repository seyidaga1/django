from django.shortcuts import render, redirect
from .models import Listing

# Home page view
def home_page(request):
    cars = Listing.objects.all()  
    return render(request, 'home.html', {'cars': cars})

# Car details view
def car_view(request, car_id):
    car = Listing.objects.get(id=car_id)  
    return render(request, 'car_detail.html', {'car': car})

# Add car view
def add_car(request):
    if request.method == 'POST':
        title = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('description')
        image = request.FILES.get('image')  

        
        Listing.objects.create(
            title=title,
            price=price,
            description=description,
            image=image,
        )
        return redirect('home')  

    return render(request, 'add_car.html')
