
from django.shortcuts import render, redirect
from .models import Hotel
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import DiningForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def hotels_index(request):
    hotels = Hotel.objects.filter(user=request.user)
    return render(request, 'hotels/index.html', {'hotels': hotels})

@login_required
def hotels_detail(request, hotel_id):
    hotel = Hotel.objects.get(id=hotel_id)
    dining_form = DiningForm()
    return render(request, 'hotels/detail.html', {
        'hotel': hotel,
        'dining_form': dining_form
        })

@login_required
def add_dining(request, hotel_id):
    form = DiningForm(request.POST)
    if form.is_valid():
        new_dining = form.save(commit=False)
        new_dining.hotel_id = hotel_id
        new_dining.save()
    return redirect('detail', hotel_id=hotel_id)    

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

class HotelCreate(LoginRequiredMixin, CreateView):
    model = Hotel
    fields = ['name', 'location', 'description', 'night']
    success_url = '/hotels/'
    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form)

class HotelUpdate(LoginRequiredMixin, UpdateView):
    model = Hotel
    fields = ['location', 'description', 'night']

class HotelDelete(LoginRequiredMixin, DeleteView):
    model = Hotel
    success_url = '/hotels/'