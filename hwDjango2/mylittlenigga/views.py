from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.contrib.auth.forms import AuthenticationForm
# Create your views here.
from .forms import AdForm, Comment, SignUpForm, CommentForm
from .models import Ad, Comment
from django.core.signing import Signer


def check(request, username):
    if request.user.is_authenticated:
        return HttpResponse(status=404)
    try:
        signer = Signer()
        checked_name = signer.unsign(username)
        user = get_object_or_404(User, username=checked_name)
        print(user.username)
        if user.is_active:
            return HttpResponse('U already activated')
        user.is_active = True
        user.save()
        print('user')
        return HttpResponse('U hgay')
    except Exception as e:
        print(e)
        return HttpResponse(status=400)


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('ad_list')
    template_name = 'accounts/signup.html'

class UserLoginView(LoginView):
    template_name = 'accounts/login.html'
    redirect_field_name = 'next'
    next_page = reverse_lazy('ad_list')
    authentication_form = AuthenticationForm

class UserLogoutView(LogoutView):
    template_name = 'accounts/logout.html'
    redirect_field_name = 'next'






class AdList(ListView):
    """
    Give list of ads
    """

    model = Ad
    context_object_name = 'ads'

class AdDetail(DetailView):
    """
    Give one ad detail
    """

    model = Ad
    context_object_name = 'ad'


class AdCreate(CreateView):
    """
    Create ad model
    """
    model = Ad
    form_class = AdForm
    template_name = 'mylittlenigga/form.html'
    success_url = '/ad/{id}'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class AdUpdate(UserPassesTestMixin, UpdateView):
    """
    Update ad model View
    """
    model = Ad
    template_name = 'mylittlenigga/form.html'
    fields = ['title', 'info', 'img']
    success_url = '/ad/{id}'

    def test_func(self):
        user = self.request.user
        object = self.get_object().author
        return user == object

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ad = self.get_object()
        form = self.get_form_class()(instance=ad)
        context['form'] = form
        return context


class AdDelete(UserPassesTestMixin, DeleteView):
    """
    Delete ad view
    """
    model = Ad
    template_name = 'mylittlenigga/form.html'
    success_url = reverse_lazy('')

    def test_func(self):
        user = self.request.user
        object = self.get_object().author
        return user == object



class CommentCreate(CreateView):
    """
    Create ad model
    """
    model = Comment
    form_class = CommentForm
    template_name = 'mylittlenigga/form.html'
    success_url = '/ad/{id}'

    def form_valid(self, form):
        form.instance.ad = get_object_or_404(Ad, pk=self.kwargs['pk']) #Bh1
        return super().form_valid(form) #Ka1