from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Category
class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, max_length=255)

    def get_absolute_url(self):
        return reverse('category_list', args=[self.slug])

    def __str__(self):
        return self.name


# Region
class Region(models.Model):
    region = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, unique=True)

    def get_absolute_url(self):
        return reverse('region_list', args=[self.slug])

    def __str__(self):
        return self.region


# Education
class Education(models.Model):
    DEGREE = (
        ('bachelor', 'bachelor'),
        ('master', 'master'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profession = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    degree = models.CharField(choices=DEGREE,max_length=20)
    university = models.CharField(max_length=255)
    years = models.CharField(max_length=20)

    def __str__(self):
        return self.profession


# Experience
class Experience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job_name = models.CharField(max_length=100)
    job_position = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    years = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created_at',)

    def __str__(self):
        return self.job_name


# Skills
class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    percentage = models.PositiveIntegerField()
    experience = models.PositiveIntegerField(help_text='how many years')

    def __str__(self):
        return self.name


# Portfolio
class Portfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(default='d1.png', blank=True, null=True)
    link = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created_at',)

    def __str__(self):
        return self.name


# Message
class Message(models.Model):
    user_sender = models.CharField(max_length=50)
    user_receiver = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.body


# Profile
class Profile(models.Model):
    GENDER = (
        ("Erkek", 'Erkek'),
        ("Zenan", 'Zenan'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    birthday = models.DateField(auto_now=False, auto_now_add=False)
    image = models.ImageField(default='default.png')
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=100)
    mobile = models.CharField(max_length=30)
    github = models.CharField(max_length=255, null=True, blank=True)
    instagram = models.CharField(max_length=255, null=True, blank=True)
    telegram = models.CharField(max_length=255, null=True, blank=True)
    facebook = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(choices=GENDER, max_length=10)
    additional = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# Post
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()
    image = models.ImageField(default='all-in-one-logos_white.png', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title


class JobType(models.Model):
    name = models.CharField(max_length=10)
    slug = models.SlugField(unique=True, max_length=20)

    def get_absolute_url(self):
        return reverse('jobtypes', args=[self.slug])

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(default='post.png', blank=True, null=True)
    skills = models.CharField(max_length=200)
    salary = models.CharField(max_length=20)
    types = models.ForeignKey(JobType, on_delete=models.SET_NULL, null=True)
    published = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-published',)

    # def get_absolute_urls(self):
    #     return reverse('category', args=[self.slug])

    def __str__(self):
        return self.title
