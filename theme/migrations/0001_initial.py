# Generated by Django 3.2 on 2022-04-08 11:42

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
            name='Fee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField()),
                ('discount', models.IntegerField()),
                ('payable', models.IntegerField()),
                ('remaining', models.IntegerField()),
                ('status', models.CharField(max_length=10)),
                ('installment', models.BooleanField()),
                ('created_at', models.DateField(default=django.utils.timezone.now)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='MembershipCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=25)),
                ('category_class', models.CharField(max_length=20)),
                ('category_months', models.CharField(max_length=15)),
                ('category_fee', models.IntegerField()),
                ('category_gender', models.CharField(max_length=15)),
                ('category_created_at', models.DateField(default=django.utils.timezone.now)),
                ('category_updated_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_amount', models.FloatField()),
                ('payment_created_at', models.DateField(default=django.utils.timezone.now)),
                ('payment_updated_at', models.DateField(auto_now=True)),
                ('fee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fee_id', to='theme.fee')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_name', models.CharField(max_length=25)),
                ('member_father_name', models.CharField(max_length=25)),
                ('member_cnic', models.CharField(max_length=16, null=True)),
                ('member_contact', models.CharField(max_length=12)),
                ('member_emergency_contact', models.CharField(max_length=12, null=True)),
                ('member_email', models.EmailField(max_length=254, null=True)),
                ('member_occupation', models.CharField(max_length=25, null=True)),
                ('member_address', models.CharField(max_length=255, null=True)),
                ('member_gender', models.CharField(max_length=10)),
                ('member_dob', models.DateField(null=True)),
                ('member_age', models.IntegerField(null=True)),
                ('member_blood_group', models.CharField(max_length=4, null=True)),
                ('member_height', models.CharField(max_length=5, null=True)),
                ('member_weight', models.IntegerField(null=True)),
                ('member_card_id', models.CharField(max_length=20)),
                ('member_target', models.CharField(max_length=100, null=True)),
                ('member_serial_no', models.CharField(max_length=20)),
                ('member_image', models.ImageField(blank=True, null=True, upload_to='profile_images/')),
                ('member_created_at', models.DateField(default=django.utils.timezone.now)),
                ('member_updated_at', models.DateField(auto_now=True)),
                ('member_membership_start_date', models.DateField()),
                ('member_membership_expiry_date', models.DateField()),
                ('active_fee_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='active_fee', to='theme.fee')),
                ('attended_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='attended_by', to='employees.employeerecord')),
                ('member_membership_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='member_membership_id', to='theme.membershipcategory')),
            ],
        ),
        migrations.AddField(
            model_name='fee',
            name='member_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='member_id', to='theme.member'),
        ),
        migrations.CreateModel(
            name='BodyAssesments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.CharField(default=0, max_length=20)),
                ('weight', models.CharField(default=0, max_length=20)),
                ('neck', models.CharField(max_length=20)),
                ('shoulder', models.CharField(max_length=20)),
                ('chest_extended', models.CharField(max_length=20)),
                ('chest_normal', models.CharField(max_length=20)),
                ('forearms', models.CharField(max_length=20)),
                ('biceps', models.CharField(max_length=20)),
                ('wrist', models.CharField(max_length=20)),
                ('upper_abs', models.CharField(max_length=20)),
                ('lower_abs', models.CharField(max_length=20)),
                ('waist', models.CharField(max_length=20)),
                ('hip', models.CharField(max_length=20)),
                ('thigh', models.CharField(max_length=20)),
                ('calves', models.CharField(max_length=20)),
                ('ankles', models.CharField(max_length=20)),
                ('body_fat', models.CharField(max_length=20)),
                ('vascular', models.CharField(max_length=20)),
                ('medical_issue', models.CharField(max_length=40)),
                ('body_target', models.CharField(max_length=30)),
                ('assesment_date', models.DateTimeField(auto_now_add=True)),
                ('member_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theme.member')),
            ],
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('amount', models.FloatField()),
                ('discount', models.FloatField()),
                ('payable', models.FloatField()),
                ('remaining', models.FloatField()),
                ('paid', models.FloatField()),
                ('bill_created_at', models.DateField(default=django.utils.timezone.now)),
                ('bill_updated_at', models.DateField(auto_now=True)),
                ('bill_attended_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bill_attended_by', to='employees.employeerecord')),
                ('fee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bill_fee_id', to='theme.fee')),
                ('member_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bill_member_id', to='theme.member')),
                ('subscription_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscription', to='theme.membershipcategory')),
            ],
        ),
    ]
