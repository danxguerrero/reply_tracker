from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Reply

from datetime import date
# Create your views here.

class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('replies')

class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('replies')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('replies')
        return super(RegisterPage, self).get(*args, **kwargs)

class ReplyList(LoginRequiredMixin, ListView):
    model = Reply
    context_object_name = 'replies'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['replies'] = context['replies'].filter(user=self.request.user)
        
        search_input = self.request.GET.get('search-area')
        if search_input:
            context['replies'] = context['replies'].filter(created__icontains=search_input)
            context['search_input'] = search_input
        else:
            context['replies'] = context['replies'].filter(created__icontains=date.today())
            context['search_input'] = date.today()
            
        context['count'] = context['replies'].count()
        

        return context 
    

class ReplyDetail(LoginRequiredMixin, DetailView):
    model = Reply
    context_object_name = 'reply'
    template_name = 'base/reply.html'

class ReplyCreate(LoginRequiredMixin, CreateView):
    model = Reply
    fields = ['ticket', 'note']
    success_url = reverse_lazy('replies')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ReplyCreate, self).form_valid(form)

class ReplyUpdate(LoginRequiredMixin, UpdateView):
    model = Reply
    fields = ['ticket', 'note']
    success_url = reverse_lazy('replies')

class DeleteView (LoginRequiredMixin, DeleteView):
    model = Reply
    context_object_name = 'reply'
    success_url = reverse_lazy('replies')