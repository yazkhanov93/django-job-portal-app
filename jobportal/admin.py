from django.contrib import admin
from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ['region', 'slug']
    prepopulated_fields = {'slug': ('region',)}


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['user','profession', 'department', 'degree']


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['job_name', 'company']


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'percentage', 'experience']


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']


@admin.register(Message)
class Message(admin.ModelAdmin):
    list_display = ['user_sender', 'user_receiver', 'created_at']


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'surname']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'created_at', 'updated']


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'region', 'skills', 'salary']


@admin.register(JobType)
class JobTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
