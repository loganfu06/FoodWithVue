from django.urls import path

from . import views

app_name = "food"

urlpatterns = [
    path("", views.FoodListView.as_view(), name="food_list"),
    path("<int:pk>", views.FoodDetailView.as_view(), name="food_detail"),
    path("new", views.FoodCreateView.as_view(), name="food_create"),
    path("update/<int:pk>", views.FoodUpdateView.as_view(),
         name="food_update"),
    path("delete/<int:pk>", views.FoodDeleteView.as_view(),
         name="food_delete"),
]