# Generated by Django 2.2.7 on 2020-01-24 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('performance', '0003_auto_20200122_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pre_primary_performance',
            name='Student_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='school.Pre_primary'),
        ),
    ]