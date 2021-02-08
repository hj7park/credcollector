from creds_app.forms import URLForm
from django.shortcuts import render,redirect
from django.urls import reverse
from .models import Cred,URL
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView
# View functions

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def creds_index(request):
  creds = Cred.objects.all()
  return render(request, 'creds/index.html', { 'creds': creds })

def creds_detail(request, cred_id):
  cred = Cred.objects.get(id=cred_id)
  urls = URL.objects.exclude(id__in = cred.url.all().values_list('id'))
  context = {'cred':cred, 'urls':urls}
  return render(request, 'creds/detail.html', context)

class CredCreate(CreateView):
    model = Cred
    fields = ['account','password','description']
    success_url = '/creds/'

class CredUpdate(UpdateView):
    model = Cred
    fields = ['account','password','description']

class CredDelete(DeleteView):
    model = Cred
    success_url = '/creds/'

# class URLCreate(CreateView):
#     model = URL
#     fields = ['url']
    
#     def get_success_url(self):
#       return reverse('detail', kwargs={'cred_id': self.kwargs['pk']})

#     def form_valid(self, form):
#       form.instance.cred_id = self.kwargs['pk']
#       return super().form_valid(form)

# class URLDelete(DeleteView):
#     model = URL
#     def get_success_url(self):
#         return reverse('detail', kwargs={'cred_id': self.kwargs['pk']})


class URLList(ListView):
  model = URL

class URLDetail(DetailView):
  model = URL

class URLCreate(CreateView):
  model = URL
  fields = ['url']

class URLUpdate(UpdateView):
  model = URL
  fields = ['url']

class URLDelete(DeleteView):
  model = URL
  success_url = '/urls/'

def add_URL_to_Cred(request, cred_id, url_id):
  Cred.objects.get(id=cred_id).url.add(url_id)
  return redirect('detail',cred_id=cred_id)

def remove_URL_to_Cred(request, cred_id, url_id):
  Cred.objects.get(id=cred_id).url.remove(url_id)
  return redirect('detail', cred_id=cred_id)
