from django.contrib import admin
from django.urls import path
from .import views as v

urlpatterns = [
    path('', v.home),
    path('addemp', v.add_emp),
    path("elist",v.emp_list),
    path('addacc', v.add_account),
    path("alist",v.account_list),
    path('delete',v.delete_emp),
    path('edit/<int:id>',v.edit_emp),
]