# Generated by Django 4.2.7 on 2023-11-11 12:51

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('E', 'Electronic'), ('F', 'Furniture'), ('O', 'Other')], max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(max_length=255)),
                ('second_name', models.CharField(max_length=255)),
                ('role', models.CharField(max_length=100)),
                ('access', models.CharField(max_length=100)),
                ('login', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('items', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('current_location', models.CharField(max_length=255)),
                ('expected_location', models.CharField(max_length=255)),
                ('expected_time', models.DateTimeField()),
                ('description', models.TextField()),
                ('sender_name', models.CharField(max_length=100)),
                ('recipient_name', models.CharField(max_length=100)),
                ('quantity', models.PositiveIntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventarization.category')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_items', to='inventarization.employee')),
                ('processed_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='processed_items', to='inventarization.employee')),
            ],
        ),
    ]
