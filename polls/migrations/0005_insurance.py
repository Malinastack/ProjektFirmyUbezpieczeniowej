# Generated by Django 4.0.1 on 2022-02-08 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_car_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Insurance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('policy_number', models.CharField(max_length=30)),
                ('policy_type', models.CharField(choices=[('NNW', 'NNW'), ('Autocasco', 'Autocasco'), ('Assistance', 'Assistance'), ('OC', 'OC')], default='OC', max_length=10)),
                ('policy_end_date', models.DateField()),
            ],
        ),
    ]
