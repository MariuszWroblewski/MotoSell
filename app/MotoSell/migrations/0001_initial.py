# Generated by Django 4.0.6 on 2022-08-09 08:21

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
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('category', models.CharField(choices=[('osobowy', 'Osobowy'), ('motocykl', 'Motocykl'), ('ciezarowy', 'Ciężarowy')], default='osobowy', max_length=16)),
                ('brand', models.CharField(max_length=32)),
                ('model', models.CharField(max_length=32)),
                ('production_year', models.IntegerField()),
                ('mileage', models.IntegerField()),
                ('capacity', models.IntegerField()),
                ('power', models.IntegerField()),
                ('fuel', models.CharField(choices=[('pb', 'Benzyna'), ('on', 'Diesel'), ('lpg', 'LPG')], max_length=8)),
                ('image', models.ImageField(null=True, upload_to='images/')),
                ('add_date', models.DateField()),
                ('pub_date', models.DateField(blank=True, null=True)),
                ('is_publicated', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
