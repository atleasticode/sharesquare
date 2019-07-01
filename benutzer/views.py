from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import BenutzerRegistrierung, BenutzerUpdate, ProfilUpdate

def registrierung(request):
    if request.method == 'POST':
        form = BenutzerRegistrierung(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hallo {username}, dein Account wurde angelegt!')
            return redirect('login')
    else:
        form = BenutzerRegistrierung()
    return render(request, 'benutzer/registrierung.html', {'form': form})

@login_required
def profil(request):
    if request.method == 'POST':
        b_update = BenutzerUpdate(request.POST, instance=request.user)
        p_update = ProfilUpdate(request.POST, request.FILES, instance=request.user.profil)
        if b_update.is_valid() and p_update.is_valid():
            b_update.save()
            p_update.save()
            messages.success(request, f'Deine Accountinformationen wurden aktualisiert.')
            return redirect('profil')

    else:
        b_update = BenutzerUpdate(instance=request.user)
        p_update = ProfilUpdate(instance=request.user.profil)

    context = {
        'b_update': b_update,
        'p_update': p_update
    }

    return render(request, 'benutzer/profil.html', context)
