# Generated by Django 4.0.6 on 2022-08-18 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MotoSell', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='is_deleted',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='is_pub',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='pub_date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]
