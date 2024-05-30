from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib import messages


from .models import *
from .forms import *

def home(request):
    
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')


def recette(request):
    messages.add_message(request, messages.INFO, "Hello world, Hope you are doing well.")
    list_rec = Recette.objects.all()
    p_data = Paginator(list_rec, 8)
    p_data_num = request.GET.get("page")
    datas = p_data.get_page(p_data_num)

    for i in list_rec:
        print(i)
    return render(request, 'pages/recette.html', {"recettes" : datas, 'messages' : messages})

#  Rec Deatil
@login_required
def rec_details(request, rec_id):
    rec = Recette.objects.get(id=rec_id)
   
    return render(request, 'pages/details.html', {"rec" : rec})


def guide(request):
    return render(request, 'pages/guide.html')

def conseil(request):
    return render(request, 'pages/conseil.html')

@login_required
@permission_required('pages.add_recette', raise_exception=True)
def creer_recette(request):
    if request.method == 'POST':
        form = RecetteForm(request.POST, request.FILES)
        if form.is_valid():
            recette = form.save(commit=False)
            recette.user_crea = request.user
            recette.save()
            # img_obj = form.instance \\ { "img" : img_obj }

            return redirect('pages:recette')
    else:
        form = RecetteForm(request.GET)
    return render(request, 'pages/insertRecette.html', {'form': form, "pageTitle" : "Creation Recette"})

@permission_required('pages.change_recette', raise_exception=True)
def mod_recette(request, rec_id):
    recette = get_object_or_404(Recette, id=rec_id)
    title = "Modifier "+ recette.nom

    if request.method == "POST":
        form = RecetteForm(request.POST, request.FILES, instance=recette)
        if form.is_valid():
            form.save()
            return redirect('pages:recette')
    else:
        form = RecetteForm(instance=recette)
    return render(request, 'pages/updateRecette.html', {'form': form, "title": title})

@permission_required('pages.delete_recette', raise_exception=True)
def suppr_recette(request, rec_id):
    recette = get_object_or_404(Recette, id=rec_id)
    
    if request.method == "POST":
        recette.delete()
        return redirect('/')
    
    return render(request, 'pages/del_recette.html', {'recette': recette })
