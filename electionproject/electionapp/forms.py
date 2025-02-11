from django import forms
from .models import *


# user reg

class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = UserRegisterModel
        fields = '__all__'
        widgets={
            'verify_user': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class UserLoginForm(forms.ModelForm):
    class Meta:
        model = UserLoginModel
        fields = '__all__'


class ReportIssueForm(forms.ModelForm):
    class Meta:
        model = ReportIssueModel
        fields = '__all__'
        widgets={
        }

class SuggestionForm(forms.ModelForm):
    class Meta:
        model = SuggestionModel
        fields = '__all__'
        widgets={
        }


class VoterAddForm(forms.ModelForm):
    class Meta:
        model = VoterAddModel
        fields = '__all__'

    
class AddSocialForm(forms.ModelForm):
    class Meta:
        model = AddSocialModel
        fields = '__all__'
        widgets={
            
        }

    
class DistrictForm(forms.Form):
    id1 = forms.IntegerField()
    district = forms.CharField(max_length=100)


class LocalForm(forms.Form):
    id2 = forms.IntegerField()
    localbody = forms.CharField(max_length=200)


class WardForm(forms.Form):
    id3 = forms.IntegerField()
    ward = forms.CharField(max_length=200)
    dis_id = models.IntegerField()
    loc_id = models.IntegerField()


class PollingForm(forms.Form):
    id4 = forms.IntegerField()
    polling = forms.CharField(max_length=200)


class ExcelForm(forms.Form):
    excel_file = forms.FileField()
    poll_id = models.IntegerField()
    dis_id = models.IntegerField()
    loc_id = models.IntegerField()
    wrd_id = models.IntegerField()


class CommentForm(forms.ModelForm):
    class Meta:
        model=CommentModel
        fields='__all__'
        widgets={
        }


class SuperMemberForm(forms.ModelForm):
    class Meta:
        model=SuperMemberModel
        fields='__all__'
        widgets={
            'verified': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class PresidentForm(forms.ModelForm):
    class Meta:
        model=PresidentModel
        fields='__all__'
        widgets={
            
        }


class AdminForm(forms.ModelForm):
    class Meta:
        model=AdminModel
        fields='__all__'
        widgets={
            'verify_user': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class AssignTaskForm(forms.ModelForm):
    class Meta:
        model=AssignTaskModel
        fields='__all__'
        widgets={
        }

    
