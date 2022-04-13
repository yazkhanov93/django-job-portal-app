import django_filters
from .models import Vacancy

class VacancyFilter(django_filters.FilterSet):
	class Meta:
		model = Vacancy
		fields = ['title', 'region', 'category']

		