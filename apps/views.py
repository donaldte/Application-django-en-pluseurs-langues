from django.shortcuts import render
from django.utils.translation import gettext as _

# Create your views here.
def home(request):
    var = _("welcome")
    return render(request, 'index.html', {'var':var})

"""
Etapes de translations
1 Definir les variables a traduires 
python manage.py makemessages -l la langue
2 C'est de donner leurs equivalences dans les a traduire 
3 Compiler 
pythom manage.py compilemessages

"""    
