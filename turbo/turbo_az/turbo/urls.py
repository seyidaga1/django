from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', views.home_page, name='home'),  # Home page
    path("home/",views.home_page , name = 'home'),
    path('car_detail/<int:car_id>/', views.car_view, name='car_detail'),  # Car detail view
    path('add_car/', views.add_car, name='add_car'),  # Add car page
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)