from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .models import Contact
from django.urls import reverse_lazy
from django.db.models import Q
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import ContactForm

def showtotal(request):
    counts= Contact.objects.all().count()
    context= {'counts': counts}
    return render(request, 'contacts/admin.html', context)

def adminview(request):
    context  = {
        'posts': Contact.objects.all()
    }
    return render(request, 'contacts/admin.html', context)

# def trashview(request):
#     context  = {
#         'posts': Trash.objects.all()
#     }
#     return render(request, 'contacts/trashadmin.html', context)

class ContactView(LoginRequiredMixin, ListView):
    model = Contact
    template_name = 'contacts/admin.html'
    context_object_name = 'posts'
    paginate_by = 12


def search(request):
    template_name = 'contacts/search.html'
    paginate_by = 12
    query = request.GET.get("q")
    posts_filter = Contact.objects.filter(
                Q(name__icontains=query)|
                Q(sbu__icontains=query)|
                Q(status__icontains=query)|
                Q(sex__icontains=query)|
                Q(email__icontains=query)|
                Q(company__icontains=query)|
                Q(position__icontains=query)
                ).distinct()
    context  = {
        'postsfilter': posts_filter,
    }
    return render(request, 'contacts/search.html', context)

# class TrashView(LoginRequiredMixin, ListView):
#     model = Trash
#     template_name = 'contacts/trashadmin.html'
#     context_object_name = 'posts'
#     paginate_by = 12


class ContactDetail(DetailView):
    model = Contact

# class TrashDetail(DetailView):
#     model = Trash

class ContactCreate(LoginRequiredMixin, CreateView):
    model = Contact
    fields = ['name', 'email', 'phone', 'address', 'sex', 'sbu', 'position', 'status', 'company']

# class TrashCreate(LoginRequiredMixin, CreateView):
#     model = Trash
#     fields = ['name', 'email', 'phone', 'address', 'sex', 'sbu', 'position', 'status', 'company']

class ContactUpdate(LoginRequiredMixin, UpdateView):
    model = Contact
    fields = ['name', 'email', 'phone', 'address', 'sex', 'sbu', 'position', 'status', 'company']

# class TrashUpdate(LoginRequiredMixin, UpdateView):
#     model = Trash
#     fields = ['name', 'email', 'phone', 'address', 'sex', 'sbu', 'position', 'status', 'company']

class ContactDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Contact
    success_url = reverse_lazy('adminview')
    success_message = " CONTACT DELETED SUCCESSFULLY"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(ContactDelete, self).delete(request, *args, **kwargs)


# class TrashDelete(LoginRequiredMixin, DeleteView):
#     model = Trash
#     success_url = 'trashview'
