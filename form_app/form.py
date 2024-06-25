from django import forms
from django.forms.widgets import NumberInput
import datetime


BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']

FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]


FAVORITE_SECONDARY_COLORS_CHOICES = [
    ('steel_blue', 'Steel-Blue'),
    ('lime_green', 'Lime-Green'),
    ('slate_blue', 'Slate-Blue'),
]



FAVORITE_SECONDARY_FOOD_CHOICES = [
    ('chocolate', 'Chocolate'),
    ('vanilla', 'Vanilla'),
    ('strawberry', 'Strawberry'),
]




FAVORITE_DRINKS_CHOICES = [
    ('coffee', 'Coffee'),
    ('tea', 'Tea'),
    ('juice', 'Juice'),
]



class NormalForm(forms.Form):
    agree = forms.BooleanField(initial=True)
    first_name = forms.CharField(initial='Your first name')
    last_name = forms.CharField(label="Enter your Name:",initial='Your last name')
    email_address = forms.EmailField( required = True,label="Please enter your email address",)
    # comment = forms.CharField(widget=forms.Textarea)
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    date = forms.DateField()
    birth_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    value = forms.DecimalField()
    message = forms.CharField(max_length = 10)
    day = forms.DateField(initial=datetime.date.today)
    favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
    secondary_favorite_colors = forms.MultipleChoiceField(choices=FAVORITE_SECONDARY_COLORS_CHOICES)
    favorite_food = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_SECONDARY_FOOD_CHOICES)
    favorite_drinks = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=FAVORITE_DRINKS_CHOICES,
    )
    favourite_number = forms.IntegerField( 
                     help_text = "Enter your favourite number number"
                     ) 
    password = forms.CharField(widget = forms.PasswordInput()) 