from django.shortcuts import render,redirect
from .forms import *
from .models import *
# Create your views here.
def home(request):
    return render(request,'dashbord.html')




def predict(request):
    form = PredictForm()
    if request.method == 'POST':
        form = PredictForm(request.POST)
        if form.is_valid():
            # Récupérer les données entrées par l'utilisateur
            Ram = form.cleaned_data['Ram']
            Poids = form.cleaned_data['Poids']
            Touchscreen = form.cleaned_data['Touchscreen']
            Pixels_par_pouce = form.cleaned_data['Pixels_par_pouce']
            HDD = form.cleaned_data['HDD']
            SDD = form.cleaned_data['SDD']
            algo = form.cleaned_data['algo']
            
            
            if algo == 'GD':
                prcie = round(Ram*(29.66884592) + Poids*(3.34256085) + Touchscreen*(-0.18523221) + Pixels_par_pouce*(22.95053152) + HDD*1.90165562 + SDD*15.03767179 +0.2212647, 2)
            elif algo == 'GS':
                prcie = round(Ram*(4.30257021*10*2) + Poids*(3.39667931*10*2) + Touchscreen*(-1.40061893*10) + Pixels_par_pouce*(1.49855289*10) + HDD*0.229581261 + SDD*6.71210718 -391.08052829, 2)
            else:
                
                prcie = None
            
            context = {'prcie': prcie,
                       'Ram' : Ram,
                       'Poids' : Poids,
                       'Touchscreen' : Touchscreen,
                       'Pixels_par_pouce' : Pixels_par_pouce,
                       'HDD' : HDD,
                       'SDD' : SDD,
                       'algo' : algo,
                       }
            return render(request, 'predicted_price.html', context)
    context = {'form' : form}
    return render(request, 'predict_form.html', context)


def Gradient_Descent(request):
    return render(request, 'gd.html')


def Gradient_Stochaqtiue(request):
    return render(request, 'gs.html')