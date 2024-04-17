from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Order
from food.models import Food
from .forms import OrderForm

from django.forms.models import model_to_dict
from django.views import View
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.generic import TemplateView
# Create your views here.

class OrderListView(LoginRequiredMixin, ListView):
    model = Order

class OrderDetailView(LoginRequiredMixin, DetailView):
    model = Order

class OrderCreateView(LoginRequiredMixin, CreateView):
    model = Order
    fields = ['customer','total_price', 'food']


    def form_valid(self, form):
        response = super().form_valid(form)
        messages.add_message(
            self.request, messages.SUCCESS,
            'Order for "{customer}" has been created'.format(
                customer=self.object.customer))
        return response

    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       all_food = list(Food.objects.all().values())
       context["orders_list"] = dict(food=[])
       context["food_list"] = all_food
       print("context", context)
       return context
    
    def get_success_url(self):
    	return reverse_lazy("order:order_detail", args=[self.object.id])

class OrderDeleteView(LoginRequiredMixin, DeleteView):
    model = Order
    success_url = reverse_lazy("order:order_list")


    def form_valid(self, form):
        response = super().form_valid(form)
        messages.add_message(
            self.request, messages.SUCCESS,
            'Order for "{customer}" has been deleted'.format(
                customer=self.object.customer))
        return response

class OrderUpdateView(LoginRequiredMixin, UpdateView):
    model = Order
    fields = ['customer','total_price', 'food']

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.add_message(
            self.request, messages.SUCCESS,
            'Order for "{customer}" has been updated'.format(
                customer=self.object.customer))
        return response

    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       orders_dico = model_to_dict(self.object)
       food = orders_dico["food"]
       food_list = []
       for someFood in food:
           food_list.append({"id": someFood.id, "name": someFood.name, "price": someFood.price})
       orders_dico["food"] = food_list
       all_food = list(Food.objects.all().values())
       context["orders_list"] = orders_dico
       context["food_list"] = all_food
       print("context", context)
       return context
   
    def get_success_url(self):
    	return reverse_lazy("order:order_detail", args=[self.object.id])
 
class OrderDetailbisView(TemplateView):
    template_name = "orders/order_detailbis.html"
    
    def get(self, request, *args, **kwargs):
        order = get_object_or_404(Order, pk=self.kwargs["pk"])
        return super().get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        order = get_object_or_404(Order, pk=self.kwargs["pk"])
        context = super().get_context_data(**kwargs)
        orders_dico = model_to_dict(order)
        food = orders_dico["food"]
        food_list = []
        for someFood in food:
            food_list.append({"id": someFood.id, "name": someFood.name, "price": someFood.price})
        orders_dico["food"] = food_list
        context["orders_list"] = orders_dico
        context['order_id'] = self.kwargs["pk"]
        return context

class OrderDetailJsView(View):
    def get(self, request, *args, **kwargs):
        order = get_object_or_404(Order, pk=self.kwargs["pk"])
        order_js = model_to_dict(order)
        return JsonResponse({"order": order_js})
