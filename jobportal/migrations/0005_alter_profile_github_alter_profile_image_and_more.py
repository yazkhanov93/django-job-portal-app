# Generated by Django 4.0.1 on 2022-02-03 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobportal', '0004_vacancy_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='github',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.png', upload_to=''),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='salary',
            field=models.CharField(max_length=20),
        ),
    ]