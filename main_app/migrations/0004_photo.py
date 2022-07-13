# Generated by Django 4.0.6 on 2022-07-13 02:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_dining_options_hotel_user_alter_dining_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.hotel')),
            ],
        ),
    ]
