from django.shortcuts import render, redirect
from .models import Emp, Account
from .form import EmpForm, AccountForm


def home(request):
    return render(request, 'home.html')


def add_emp(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        age = request.POST.get("age")
        contact = request.POST.get("contact")
        address = request.POST.get("address")
        print('------------------>', name, email, age, contact, address)
        e = Emp()
        e.name = name
        e.email = email
        e.contact = contact
        e.age = age
        e.address = address
        e.save()
        return redirect("/")
    else:
        return render(request, "addemp.html")


def add_account(request):
    if request.method == 'POST':
        f = AccountForm(request.POST)
        f.save()
        return redirect("/")
    else:
        f = AccountForm
        d = {'form': f}
        return render(request, 'form.html', d)


def emp_list(request):
    elist = Emp.objects.all()
    d = {"el": elist}
    return render(request, "emplist.html", d)


def account_list(request):
    alist = Account.objects.all()
    d = {'al': alist}
    return render(request, "acclist.html", d)


def delete_emp(request):
    eid = request.GET.get("id")
    emp = Emp.objects.get(id=eid)
    emp.delete()
    return redirect("/elist")


def edit_emp(request, id):
    emp = Emp.objects.get(id=id)
    if request.method == 'POST':
        f = EmpForm(request.POST, instance=emp)
        f.save()
        return redirect("/elist")
    else:
        f = EmpForm(instance=emp)
        context = {'form': f}
        return render(request, "form.html", context)