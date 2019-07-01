from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Anzeige, Kategorie



def home(request):
    context = {
        'anzeigen': Anzeige.objects.all()
    }
    return render(request, 'anzeigen/home.html', context)

class AnzeigenListenAnsicht(ListView):
    model = Anzeige
    template_name = 'anzeigen/home.html'
    context_object_name = 'anzeigen'
    ordering = ['-erstellungsdatum']
    paginate_by = 8


class BenutzerAnzeigenListenAnsicht(ListView):
    model = Anzeige
    template_name = 'anzeigen/benutzer_anzeigen.html'
    context_object_name = 'anzeigen'
    ordering = ['-erstellungsdatum']
    paginate_by = 8

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Anzeige.objects.filter(autor=user).order_by('-erstellungsdatum')



class KategorienListenAnsicht(ListView):
    model = Anzeige
    template_name = 'anzeigen/anzeigen_kategorie.html'
    context_object_name = 'anzeigen'
    ordering = ['-erstellungsdatum']
    paginate_by = 8

    def get_queryset(self):
        return Anzeige.objects.filter(kategorie_id=self.kwargs.get('pk')).order_by('-erstellungsdatum')
    


class AnzeigenDetailAnsicht(DetailView):
    model = Anzeige


class AnzeigenAnlegenAnsicht(LoginRequiredMixin, CreateView):
    model = Anzeige
    fields = ['titel', 'inhalt', 'kategorie']

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)


class AnzeigenAktualisierenAnsicht(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Anzeige
    fields = ['titel', 'inhalt', 'kategorie']

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

    def test_func(self):
        anzeige = self.get_object()
        if self.request.user == anzeige.autor:
            return True
        return False


class AnzeigenLoeschenAnsicht(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Anzeige
    success_url = '/'

    def test_func(self):
        anzeige = self.get_object()
        if self.request.user == anzeige.autor:
            return True
        return False
    

def about(request):
    return render(request, 'anzeigen/about.html', {'title': 'So funktioniert es'})
