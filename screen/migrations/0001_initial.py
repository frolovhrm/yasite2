# Generated by Django 4.1.7 on 2023-03-10 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, primary_key=True, serialize=False, to='screen.user')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Screen',
            fields=[
                ('id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, primary_key=True, serialize=False, to='screen.cars')),
                ('name', models.CharField(max_length=200)),
                ('usable', models.BooleanField()),
                ('readed', models.BooleanField()),
                ('errors_log', models.CharField(max_length=30)),
                ('strline', models.CharField(max_length=1000)),
            ],
        ),
    ]
