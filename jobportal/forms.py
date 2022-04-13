from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile, Education, Experience, Skill, Post, Portfolio, Message



#message form
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['user_sender', 'user_receiver', 'body']


        widgets = {
            'body':forms.TextInput(attrs={'class':'form-control', 'placeholder':'type your message'})
        }


#portfolio form
class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['user', 'name', 'link', 'image', 'description']


        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Portfolio name'}),
            'link':forms.TextInput(attrs={'class':'form-control', 'placeholder':'url link'}),
            'description':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Description'}),
        }




#post form
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['user', 'title', 'body', 'image']

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'post title'}),
            'body': forms.Textarea(attrs={'class':'form-control','placeholder':'Text'})
        }




#add skills form
class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields= ['user','name', 'percentage', 'experience']

        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'name'}),
            'percentage':forms.TextInput(attrs={'class':'form-control', 'placeholder':'percentage %'}),
            'experience':forms.TextInput(attrs={'class':'form-control', 'placeholder':'years experience'})
        }


#add experience Form
class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['user', 'job_name', 'job_position', 'company', 'years']


        widgets = {
            'job_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'job name'}),
            'job_position':forms.TextInput(attrs={'class':'form-control', 'placeholder':'job position'}),
            'company':forms.TextInput(attrs={'class':'form-control', 'placeholder':'company name and Country'}),
            'years': forms.TextInput(attrs={'class':'form-control', 'placeholder':'years'})
        }

#add_education Form
class EducationForm(forms.ModelForm):
    # degree = forms.ChoiceField(choices=DEGREE, label='degree', widget=forms.Select(), required=True)
    class Meta:
        model = Education
        fields = ['degree', 'profession', 'department', 'user', 'university', 'years']

        widgets = {
            # 'user':forms.TextInput(attrs={'class':'form-control', 'placeholder': 'user'}),
            # 'degree':forms.CharField(attrs={'class':'form-control', 'placeholder':'degree'}),
            'profession':forms.TextInput(attrs={'class':'form-control', 'placeholder':'profession'}),
            'department':forms.TextInput(attrs={'class':'form-control', 'placeholder': 'department'}),
            'university':forms.TextInput(attrs={'class':'form-control', 'placeholder':'university name and Country'}),
            'years':forms.TextInput(attrs={'class':'form-control', 'placeholder':'years'})
        }



#profile form
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user', 'category', 'name', 'surname', 'birthday', 'image', 'region', 'address', 'mobile', 'github', 'instagram', 'telegram', 'facebook', 'gender', 'additional']

        widgets = {
            # 'category':forms.TextInput(attrs={'class':'form-control', 'placeholder':'category'}),
            'name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'first name'}),
            'surname':forms.TextInput(attrs={'class':'form-control','placeholder':'last name'}),
            'birthday':forms.TextInput(attrs={'class':'form-control', 'placeholder':'birthday'}),
            #'image':forms.TextInput(attrs={'class':'form-control', 'placeholder':'image'}),
            #'region':forms.TextInput(attrs={'class':'form-control', 'placeholder':'region'}),
            'address':forms.TextInput(attrs={'class':'form-control', 'placeholder':'address'}),
            'mobile':forms.TextInput(attrs={'class':'form-control', 'placeholder':'mobile'}),
            'github':forms.TextInput(attrs={'class':'form-control', 'placeholder':'github link'}),
            'instagram':forms.TextInput(attrs={'class':'form-control', 'placeholder':'instagram link'}),
            'telegram':forms.TextInput(attrs={'class':'form-control', 'placeholder':'telegram link'}),
            'facebook':forms.TextInput(attrs={'class':'form-control', 'placeholder':'facebook link'}),
            #'gender':forms.TextInput(attrs={'class':'form-control', 'placeholder':'gender'}),
            'additional':forms.Textarea(attrs={'class':'form-control', 'placeholder':'additional'}),
        }



#register form
class CreateUserForm(UserCreationForm):
    # username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'username'})),
    # password1 = forms.CharField(label='Password',
    #                             widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password'}))
    # password2 = forms.CharField(label='Confirm Password',
    #                             widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        #
        # widget = {
        #     'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username'}),
        #     'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'email'}),
        # }
