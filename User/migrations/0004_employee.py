# Generated by Django 2.2.6 on 2019-11-04 04:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_auto_20191031_2139'),
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('pic', models.FileField(blank=True, null=True, upload_to='')),
                ('job', models.CharField(max_length=200)),
                ('work_email', models.CharField(max_length=200)),
                ('work_mobile', models.BigIntegerField(max_length=200)),
                ('work_iemi', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('martial_status', models.CharField(max_length=200)),
                ('dob', models.DateField()),
                ('address', models.CharField(max_length=200)),
                ('mail_id', models.CharField(max_length=200)),
                ('mobile', models.BigIntegerField()),
                ('user_name', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('depart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.department')),
                ('hotels', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.hotel')),
            ],
        ),
    ]
