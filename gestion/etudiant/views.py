from django.shortcuts import render, HttpResponsePermanentRedirect, HttpResponse

from .forms import studentRegistration
from .models import User


# cette fonction  permet d'ajout et d'afficher les info des etudiants
from django.shortcuts import render, redirect

from django.contrib import messages
from .forms import studentRegistration
from .models import User

def add_show(request):
    if request.method == 'POST':
        fm = studentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            tl = fm.cleaned_data['tel']

            # Vérifier si un utilisateur avec cet email ou numéro de téléphone existe déjà
            if User.objects.filter(email=em).exists():
                messages.error(request, 'Un utilisateur avec cet email existe déjà.')
            elif User.objects.filter(tel=tl).exists():
                messages.error(request, 'Un utilisateur avec ce numéro de téléphone existe déjà.')
            else:
                # Créer un nouvel utilisateur et l'enregistrer
                reg = User(name=nm, email=em, tel=tl)
                reg.save()
                messages.success(request, 'Utilisateur ajouté avec succès.')
                return redirect('/')

        else:
            messages.error(request, 'Veuillez corriger les erreurs dans le formulaire.')

    else: 
        fm = studentRegistration()

    # Récupérer tous les utilisateurs pour les afficher
    stud = User.objects.all()
    return render(request, 'etudiant/addandshow.html', {'form': fm, 'stu': stud})


# fonction pour modifier les datas

def update_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = studentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
      
        return HttpResponsePermanentRedirect('/')
    else:
        pi = User.objects.get(id=id)
        fm = studentRegistration(instance=pi)
    return render(request, 'etudiant/update.html', {'form':fm}) 
    

# fonction pour supprimer les donnees

def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponsePermanentRedirect('/')
    

#

