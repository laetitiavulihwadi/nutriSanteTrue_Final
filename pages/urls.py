from django.contrib import admin
from django.urls import path
import pages.views as page_views


app_name = 'pages'
urlpatterns = [
    path('', page_views.home, name='home'),
    path('about/', page_views.about,name='about'),
    path('recette/', page_views.recette,name='recette'),
    path('guide/', page_views.guide,name='guide'),
    path('conseil/', page_views.conseil,name='conseil'),
    path('insert/', page_views.creer_recette,name='insertRec'),
    path('update/<int:rec_id>', page_views.mod_recette,name="updateRec"),
    path('details/<int:rec_id>', page_views.rec_details, name='details'),
    path('del/<int:rec_id>', page_views.suppr_recette, name='del_Recette'),
    
]
