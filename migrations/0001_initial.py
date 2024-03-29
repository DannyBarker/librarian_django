# Generated by Django 2.2.5 on 2019-09-18 16:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Librarian',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='librarians', to='libraryapp.Library')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('ISBN', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=50)),
                ('year_published', models.IntegerField()),
                ('librarian', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libraryapp.Librarian')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libraryapp.Library')),
            ],
        ),
    ]
