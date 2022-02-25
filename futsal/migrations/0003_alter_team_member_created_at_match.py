# Generated by Django 4.0.1 on 2022-02-25 11:27

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('futsal', '0002_alter_team_member_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='member_created_at',
            field=models.DateField(default=datetime.datetime(2022, 2, 25, 16, 27, 57, 272993)),
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now=True)),
                ('meridiem', models.CharField(max_length=5)),
                ('fee', models.IntegerField()),
                ('paid', models.IntegerField()),
                ('data', models.DateField(auto_now_add=True)),
                ('team1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team1', to='futsal.team')),
                ('team2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team2', to='futsal.team')),
            ],
        ),
    ]
