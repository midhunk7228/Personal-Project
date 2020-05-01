from django.urls import path
from . import views

urlpatterns=[

    path('Login/',views.Login),
    path('Dashboard/',views.Dashboard),
    path('add_hotel/', views.add_hotel),
    path('hotels_fields/', views.hotels_fields),
    path('hotels/', views.hotels),
    path('hotel_update/<int:id>', views.hotel_update),
    path('hotel_updated/', views.hotel_updated),
    path('hotel_delete/<int:id>', views.hotel_delete),
    path('department_add/', views.department_add),
    path('department_adding/', views.department_adding),
    path('department_list/', views.department_list),
    path('department_update/<int:id>', views.department_update),
    path('department_updated/', views.department_updated),
    path('delete_depart/<int:id>/', views.delete_depart),
    path('employee_/', views.employee_),
    path('employee_lists/', views.employee_lists),
    path('employee_delete/<int:id>', views.employee_delete),
    path('empl/', views.empl,name='empl'),
    path('search/', views.search, name='search'),
    path('employee_add/', views.employee_add, name='employee_add'),
    path('employee_update/<int:id>', views.employee_update, name='employee_update'),
    path('employee_updated/', views.employee_updated, name='employee_updated'),






]