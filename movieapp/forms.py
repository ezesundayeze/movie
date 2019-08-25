from django import forms
from movieapp.models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = "__all__"

        widgets = {
            "title":forms.TextInput(attrs={"class":"form-control", "placeholder":"Movie Title"}),
            "length":forms.NumberInput(attrs={"class":"form-control", "placeholder":"Movie Length (Hours)"}),
            "year":forms.DateInput(attrs={"class":"form-control", "placeholder":"Year", "type":"date"}),
            "language":forms.TextInput(attrs={"class":"form-control", "placeholder":"Language"}),
            "director_name":forms.TextInput(attrs={"class":"form-control", "placeholder":"Movie Director"}),
            
        }
