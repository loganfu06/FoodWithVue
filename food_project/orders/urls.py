from django.urls import path

from . import views

app_name = "order"

urlpatterns = [
    path("", views.OrderListView.as_view(), name="order_list"),
    path("<int:pk>", views.OrderDetailView.as_view(), name="order_detail"),
    path("new", views.OrderCreateView.as_view(), name="order_create"),
    path("update/<int:pk>", views.OrderUpdateView.as_view(),
         name="order_update"),
    path("delete/<int:pk>", views.OrderDeleteView.as_view(),
         name="order_delete"),
    path("bis/<int:pk>", views.OrderDetailbisView.as_view(), name="order_detail_bis",),
    path( "js/<int:pk>", views.OrderDetailJsView.as_view(), name="order_detail_js", ),
]