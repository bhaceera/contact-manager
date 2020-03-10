from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .models import Contact, Customer
from django.urls import reverse_lazy
from django.db.models import Count, Q
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import ContactForm, CustomerForm
from django.conf import settings


def adminview(request):
    context  = {
        'posts': Contact.objects.all()
    }
    return render(request, 'contacts/admin.html', context)



class ContactView(LoginRequiredMixin, ListView):
    model = Contact
    template_name = 'contacts/admin.html'
    context_object_name = 'posts'
    paginate_by = 12


class CustomerView(LoginRequiredMixin, ListView):
    model = Customer
    template_name = 'contacts/admin.html'
    context_object_name = 'posts'
    paginate_by = 12


def search(request):
    template_name = 'contacts/search.html'
    paginate_by = 12
    success_message = " CONTACT DELETED SUCCESSFULLY"
    query = request.GET.get("q")
    posts_filter = Contact.objects.filter(
                Q(name__icontains=query)|
                Q(sbu__icontains=query)|
                Q(status__icontains=query)|
                Q(sex__icontains=query)|
                Q(email__icontains=query)|
                Q(position__icontains=query)
                ).distinct()
    context  = {
        'postsfilter': posts_filter,
    }

    if posts_filter == "":
        messages.success(request, success_message)
    else:
        return render(request, 'contacts/search.html', context)


class ContactDetail(DetailView):
    model = Contact


class CustomerDetail(DetailView):
    model = Customer


class ContactCreate(LoginRequiredMixin, CreateView):
    model = Contact
    fields = ['name', 'email', 'phone', 'address', 'sex', 'sbu', 'position', 'status']


class CustomerCreate(LoginRequiredMixin, CreateView):
    model = Customer
    fields = ['name', 'email', 'phone', 'address', 'sex', 'sbu', 'position', 'company']


class ContactUpdate(LoginRequiredMixin, UpdateView):
    model = Contact
    fields = ['name', 'email', 'phone', 'address', 'sex', 'sbu', 'position', 'status']

class CustomerUpdate(LoginRequiredMixin, UpdateView):
    model = Customer
    fields = ['name', 'email', 'phone', 'address', 'sex', 'sbu', 'position', 'company']



class ContactDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Contact
    success_url = reverse_lazy('adminview')
    success_message = " CONTACT DELETED SUCCESSFULLY"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(ContactDelete, self).delete(request, *args, **kwargs)




class CustomerDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Customer
    success_url = reverse_lazy('adminview')
    success_message = " CONTACT DELETED SUCCESSFULLY"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(CustomerDelete, self).delete(request, *args, **kwargs)
