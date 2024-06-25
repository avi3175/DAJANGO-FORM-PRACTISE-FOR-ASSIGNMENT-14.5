from django.shortcuts import render, HttpResponse
from .form import NormalForm

def home(request):
    normal_form = NormalForm()  # Instantiate the form outside the if block
    if request.method == 'POST':
        normal_form = NormalForm(request.POST)
        if normal_form.is_valid():
            print(normal_form.cleaned_data)
            # Process the form data or save it to the database
    
    # Always pass the form to the template, whether POST or not
    return render(request, 'form_app/home.html', {'form': normal_form})



