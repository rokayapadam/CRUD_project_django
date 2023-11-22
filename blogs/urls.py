from django.urls import path
from . import views
urlpatterns = [
    path('delete<int:id>', views.delete_view, name='delete'),
    path('<int:id>', views.update_view, name='update')
   
]