# Generated by Django 3.0 on 2021-10-26 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicants', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteer',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='volunteer',
            name='days_available',
            field=models.CharField(choices=[('MON', 'Monday'), ('TUE', 'Tuesday'), ('WED', 'Wednesday'), ('THU', 'Thursday'), ('FRI', 'Friday'), ('SAT', 'Saturday'), ('SUN', 'Sunday')], default='SAT', max_length=3),
        ),
        migrations.AddField(
            model_name='volunteer',
            name='first_name',
            field=models.CharField(default='n/a', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='volunteer',
            name='last_name',
            field=models.CharField(default='n/a', max_length=20),
            preserve_default=False,
        ),
    ]
