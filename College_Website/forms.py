from django import forms

from College_Website.models import St_Registration

class LoginForm(forms.Form):
    register_number = forms.CharField(max_length=20, label='Register Number')
    date_of_birth = forms.DateField(label='Date of Birth', widget=forms.DateInput(attrs={'type': 'date'}))

    widgets={
        'register_number':forms.TextInput(attrs={'class':'form-control'}),
        'date_of_birth':forms.TextInput(attrs={'class':'form-control'}),
        
    }
    
    
class REG_FORM(forms.ModelForm):
    
    class Meta:
        model = St_Registration
        fields =['Name','Fathers_name', 'DOB','Age','Reg_number','Address','Gender','Department','Blood_Group','image']
        
    # widgets={
    #     'Name':forms.TextInput(attrs={'class':'form-control'}),
    #     'Fathers_name':forms.TextInput(attrs={'class':'form-control'}),
    #     'DOB':forms.DateInput(attrs={'class':'form-control'}),
    #     'Age':forms.TextInput(attrs={'class':'form-control'}),
    #     'Reg_number':forms.TextInput(attrs={'class':'form-control'}),
    #     'Address':forms.TextInput(attrs={'class':'form-control'}),
    #     'Gender':forms.RadioSelect(attrs={'class':'form-control'}),
    #     'Department':forms.ChoiceField(attrs={'class':'form-control'}),
    #     'Blood_Group':forms.ChoiceField(attrs={'class':'form-control'}),
    #     'image':forms.ImageField(attrs={'class':'form-control'}),
        
    # }

        
    
    
