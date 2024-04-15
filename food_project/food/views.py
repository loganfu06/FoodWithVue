from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Food
from .forms import FoodForm

from django.forms.models import model_to_dict
from django.views import View
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.generic import TemplateView
# Create your views here.

class FoodListView(LoginRequiredMixin, ListView):
    model = Food

class FoodDetailView(LoginRequiredMixin, DetailView):
    model = Food

class FoodCreateView(LoginRequiredMixin, CreateView):
    model = Food
    fields = ['name','price']

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.add_message(
            self.request, messages.SUCCESS,
            'Food "{food_name}" has been created'.format(
                food_name=self.object.name))
        return response

    def get_success_url(self):
    	return reverse_lazy("food:food_detail", args=[self.object.id])

class FoodDeleteView(LoginRequiredMixin, DeleteView):
    model = Food
    success_url = reverse_lazy("food:food_list")


    def form_valid(self, form):
        response = super().form_valid(form)
        messages.add_message(
            self.request, messages.SUCCESS,
            'Food "{food_name}" has been deleted'.format(
                food_name=self.object.name))
        return response

class FoodUpdateView(LoginRequiredMixin, UpdateView):
    model = Food
    fields = ['name','price']

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.add_message(
            self.request, messages.SUCCESS,
            'Food "{food_name}" has been updated'.format(
                food_name=self.object.name))
        return response

    def get_success_url(self):
    	return reverse_lazy("food:food_detail", args=[self.object.id])


class FoodDetailbisView(TemplateView):
    template_name = "food/food_detailbis.html"