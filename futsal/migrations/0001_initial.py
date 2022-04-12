# Generated by Django 4.0.1 on 2022-04-12 08:11

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(default='', max_length=25)),
                ('meridiem', models.CharField(max_length=5)),
                ('booking_date', models.DateField()),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=25)),
                ('captain_name', models.CharField(max_length=25)),
                ('contact_number', models.IntegerField()),
                ('member_created_at', models.DateField(default=django.utils.timezone.now)),
                ('member_updated_at', models.DateField(auto_now=True)),
                ('team_attended_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='employees.employeerecord')),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('fee', models.IntegerField()),
                ('paid', models.CharField(default='Unpaid', max_length=10)),
                ('booking_time', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking_time', to='futsal.booking')),
                ('match_attended_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='match_attended_by', to='employees.employeerecord')),
                ('team1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team1', to='futsal.team')),
                ('team2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team2', to='futsal.team')),
            ],
        ),
    ]
