from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('jobtypes/<slug:slug>/', views.jobtype, name='jobtypes'),
    path('category_list/<slug:category_slug>/', views.category_list, name='category_list'),

    #vacancy
    path('vacancy/', views.vacancy, name='vacancy'),
    path('vacancy_detail/<int:pk>/', views.vacancy_detail, name='vacancy_detail'),


    #register urls
    path('sign_up/', views.sign_up, name='sign_up'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('sign_out/', views.sign_out, name='sign_out'),

    #create profile
    path('create_profile/', views.create_profile, name='profile_form'),
    path('profile_setting/', views.profile_setting, name='profile_setting'),
    path('my_profile/', views.my_profile, name='my_profile'),
    path('profiles/', views.profiles, name='profiles'),
    path('profile_detail/<int:pk>/', views.profile_detail, name='profile_detail'),

    #education
    path('add_education/', views.add_education, name='add_education'),
    path('edit_education/<int:pk>/', views.edit_education, name='edit_education'),
    path('delte_education/<int:pk>/', views.delete_education, name='delete_education'),

    #experience
    path('add_experience/', views.add_experience, name='add_experience'),
    path('edit_experience/<int:pk>/', views.edit_experience, name='edit_experience'),
    path('delete_experience/<int:pk>/', views.delete_experience, name='delete_experience'),


    #skills
    path('add_skills/', views.add_skills, name='add_skills'),
    path('edit_skills/<int:pk>/', views.edit_skills, name='edit_skills'),
    path('delete_skill/<int:pk>/', views.delete_skills, name='delete_skills'),


    #post
    path('add_post/', views.add_post, name='add_post'),
    path('edit_post/<int:pk>/', views.edit_post, name='edit_post'),
    path('delete_post/<int:pk>/', views.delete_post, name='delete_post'),
    path('post_detail/<int:pk>/', views.post_detail, name='post_detail'),
    path('posts/', views.posts, name='posts'),


    #portfolio
    path('add_portfolio/', views.add_portfolio, name='add_portfolio'),
    path('edit_portfolio/<int:pk>/', views.edit_portfolio, name='edit_portfolio'),
    path('delete_portfolio/<int:pk>/', views.delete_portfolio, name='delete_portfolio'),


    #messages
    # path('write_message/', views.write_message, name='write_message'),
    path('messages/', views.messages, name='messages'),
    path('message_detail/<int:pk>/', views.message_detail, name='message_detail'),
    path('delete_message/<int:pk>/', views.delete_message, name='delete_message'),

]
