from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.db.models import Q

from .models import Category, Region, Skill, Education, Experience, Portfolio, Profile, Post, Message, JobType, Vacancy
from .forms import CreateUserForm, ProfileForm, EducationForm, ExperienceForm, SkillForm, PostForm, PortfolioForm, MessageForm
from .filters import VacancyFilter



# filter profiles by category
def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    profile = Profile.objects.filter(category=category)
    return render(request, 'categories.html', {'category': category, 'profile':profile})



# filter by job nature
def jobtype(request, slug):
    jobtypes = JobType.objects.all()
    jobtype = get_object_or_404(JobType, slug=slug)
    vacancy = Vacancy.objects.filter(types=jobtype)
    return render(request, 'jobtypes.html', {'jobtypes': jobtypes, 'vacancy': vacancy})


# main
def index(request):
    # count = Vacancy.objects.count()
    search = request.GET.get('search', '')
    if search:
        vacancy = Vacancy.objects.filter(Q(title__icontains=search)|Q(description__icontains=search))
    else:
        vacancy = Vacancy.objects.all()[:5]
    region = Region.objects.all()
    # vacancy_filter = VacancyFilter(request.GET, queryset=vacancy)
    # vacancy = vacancy_filter.qs
    
    message_count = Message.objects.filter(user_receiver=request.user.id, is_read=False).count()
    return render(request, 'index.html', {'vacancy': vacancy, 'region':region,'message_count':message_count})


# #regions



#vacancy
def vacancy(request):
    search = request.GET.get('search', '')
    if search:
        vacancy = Vacancy.objects.filter(Q(title__icontains=search)|Q(skills__icontains=search))
    else:
        vacancy = Vacancy.objects.all()
    return render(request, 'vacancy.html', {'vacancy':vacancy})


#vacancy deteail
def vacancy_detail(request, pk):
    vacancy = Vacancy.objects.get(id=pk)
    return render(request, 'vacancy_detail.html', {'vacancy':vacancy})


# sign up
def sign_up(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sign_in')
    return render(request, 'sign_up.html', {'form': form})


# sign in
def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if hasattr(user, 'profile'):
                return redirect('my_profile')
            else:
                return redirect('profile_form')
        else:
            messages.warning(request, 'Invalid password or username')
    return render(request, 'sign_in.html', {})


# sign out
def sign_out(request):
    logout(request)
    return redirect('index')


# create profile
def create_profile(request):
    user = get_object_or_404(User, id=request.user.id)
    profile_form = ProfileForm()
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('index')
    return render(request, 'profile_form.html', {'form': profile_form})


# profile setting
def profile_setting(request):
    profile = Profile.objects.get(user=request.user.id)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('my_profile')
    return render(request, 'profile_form.html', {'form': ProfileForm(instance=profile)})


# my profile
def my_profile(request):
    user = get_object_or_404(User, id=request.user.id)
    profile = Profile.objects.get(user=user)
    education = Education.objects.filter(user=request.user.id)
    experience = Experience.objects.filter(user=request.user.id)
    skill = Skill.objects.filter(user=request.user.id)
    post = Post.objects.filter(user=request.user.id)
    portfolio = Portfolio.objects.filter(user=request.user.id)
    message_count = Message.objects.filter(user_receiver=request.user.id, is_read=False).count()
    return render(request, 'my_profile.html', {'profile': profile, 'education':education, 'experience':experience,
                 'skill':skill, 'post':post, 'portfolio':portfolio, 'message_count':message_count})


# profiles
def profiles(request):
    search = request.GET.get('search', '')
    if search:
        profile = Profile.objects.filter(Q(name__icontains=search) | Q(surname__icontains=search))
    else:
        profile = Profile.objects.all()
    return render(request, 'profiles.html', {'profile': profile})




#profile detail
def profile_detail(request, pk):
    profile = Profile.objects.get(id=pk)
    post = Post.objects.filter(user=pk)
    portfolio = Portfolio.objects.filter(user=pk)
    skill = Skill.objects.filter(user=pk)
    education = Education.objects.filter(user=pk)
    experience = Experience.objects.filter(user=pk)
    message = MessageForm(request.POST)
    if request.method=='POST':
        form = message
        if form.is_valid():
            form.save()
            return redirect('profiles')
    return render(request, 'profile_detail.html', {'profile': profile, 'message':message, 'post':post,
                 'portfolio':portfolio, 'skill':skill, 'education':education, 'experience':experience})




#add_education
def add_education(request):
    education = EducationForm()
    if request.method=='POST':
        form = EducationForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = User.objects.get(id=request.user.id)
            obj.save()
            return redirect('my_profile')
    return render(request, 'education_form.html', {'education': education})


#edit education form
def edit_education(request,pk):
    education = Education.objects.get(id=pk)
    if request.method=='POST':
        form=EducationForm(request.POST, instance=education)
        if form.is_valid():
            form.save()
            return redirect('my_profile')
    return render(request, 'education_form.html', {'education':EducationForm(instance=education)})


#delete education 
def delete_education(request, pk):
    education = Education.objects.get(id=pk)
    education.delete()
    return redirect('my_profile')



#add experience
def add_experience(request):
    experience = ExperienceForm()
    if request.method=='POST':
        form = ExperienceForm(request.POST)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=User.objects.get(id=request.user.id)
            obj.save()
            return redirect('my_profile')
    return render(request, 'experience_form.html', {'experience':experience})


#edit experience
def edit_experience(request,pk):
    experience = Experience.objects.get(id=pk)
    if request.method=='POST':
        form = ExperienceForm(request.POST, instance=experience)
        if form.is_valid():
            form.save()
            return redirect('my_profile')
    return render(request, 'experience_form.html', {'experience':ExperienceForm(instance=experience)})



#delete experience
def delete_experience(request,pk):
    experience = Experience.objects.get(id=pk)
    experience.delete()
    return redirect('my_profile')



#add skills
def add_skills(request):
    skill = SkillForm()
    if request.method=='POST':
        form=SkillForm(request.POST)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=User.objects.get(id=request.user.id)
            obj.save()
            return redirect('my_profile')
    return render(request, 'skills_form.html', {'skill':skill})


#edit skill
def edit_skills(request, pk):
    skill = Skill.objects.get(id=pk)
    if request.method=='POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            return redirect('my_profile')
    return render(request, 'skills_form.html', {'skill':SkillForm(instance=skill)})


#delete skill
def delete_skills(request,pk):
    skill = Skill.objects.get(id=pk)
    skill.delete()
    return redirect('my_profile')



#add post
def add_post(request):
    post = PostForm()
    if request.method=='POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=User.objects.get(id=request.user.id)
            obj.save()
            return redirect('my_profile')
    return render(request, 'post_form.html', {'post':post})



#edit post
def edit_post(request, pk):
    post = Post.objects.get(id=pk)
    if request.method=='POST':
        form=PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('my_profile')
    return render(request, 'post_form.html', {'post':PostForm(instance=post)})


#delete post
def delete_post(request,pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return redirect('my_profile')


#post detail
def post_detail(request,pk):
    post = Post.objects.get(id=pk)
    return render(request, 'post_detail.html', {'post':post})



#add portfolio
def add_portfolio(request):
    portfolio = PortfolioForm()
    if request.method=='POST':
        form = PortfolioForm(request.POST, request.FILES)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=User.objects.get(id=request.user.id)
            obj.save()
            return redirect('my_profile')
    return render(request, 'portfolio_form.html', {'portfolio':portfolio})



#edit portfolio
def edit_portfolio(request,pk):
    portfolio=Portfolio.objects.get(id=pk)
    if request.method=='POST':
        form=PortfolioForm(request.POST, request.FILES, instance=portfolio)
        if form.is_valid():
            form.save()
            return redirect('my_profile')
    return render(request, 'portfolio_form.html', {'portfolio':PortfolioForm(instance=portfolio)})


#delete portfolio
def delete_portfolio(request,pk):
    portfolio = Portfolio.objects.get(id=pk)
    portfolio.delete()
    return redirect('my_profile')


#posts
def posts(request):
    search = request.GET.get('search', '')
    if search:
        post = Post.objects.filter(Q(title__icontains=search)|Q(body__icontains=search))
    else:
        post = Post.objects.all()
    return render(request, 'posts.html', {'post':post})


#messages
# def write_message(request):
#     message = MessageForm()
#     if request.method=='POST':
#         form = MessageForm(request.POST)
#         if form.is_valid():
#             obj=form.save(commit=False)
#             obj.user_receiver = Profile.objects.get(user=profile.user.id)
#             obj.save()
#             return redirect('index')
#     return render(request, 'message_form.html', {'message':message})



def messages(request):
    user = get_object_or_404(User, id=request.user.id)
    profile = Profile.objects.get(user=request.user)
    education = Education.objects.filter(user=request.user.id)
    experience = Experience.objects.filter(user=request.user.id)
    skill = Skill.objects.filter(user=request.user.id)
    messages = Message.objects.filter(user_receiver=request.user.id)
    return render(request, 'messages.html', {'messages':messages, 'profile':profile, 'experience':experience, 'skill':skill})


def message_detail(request, pk):
    message = Message.objects.get(id=pk)
    message.is_read = True
    message.save()
    return render(request, 'message_detail.html', {'message':message})



def delete_message(request, pk):
    message = Message.objects.get(id=pk)
    message.delete()
    return redirect('messages')