from django.urls import path
from .import views


urlpatterns = [
    # path('', views.HelloOrdeView.as_view(), name='hello_Order'),
    path('', views.OrderCreateListView.as_view(), name='orders'),
    path('<int:order_id>/', views.OrderDetailView.as_view(), name='order_detail'),
    path('update-status/<int:order_id>/', views.UpdateorderStatus.as_view(), name='update_status'),
    path('user/<int:user_id>/orders/', views.UserOrdersView.as_view(), name='user_orders'),
    path('user/<int:user_id>/order/<int:order_id>', views.UserOrderDetailView.as_view(), name='user_specific_detail'),
]