
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('hotels/', views.hotels_index, name='index'),
    path('hotels/<int:hotel_id>/', views.hotels_detail, name='detail'),
    path('hotels/create/', views.HotelCreate.as_view(), name='hotels_create'),
    path('hotels/<int:pk>/update/', views.HotelUpdate.as_view(), name='hotels_update'),
    path('hotels/<int:pk>/delete/', views.HotelDelete.as_view(), name='hotels_delete'),
    path('hotel/<int:hotel_id>/add_dining/', views.add_dining, name='add_dining'),
    path('accounts/signup/', views.signup, name='signup'),
    path('hotels/<int:hotel_id>/add_photo/', views.add_photo, name='add_photo'),
]