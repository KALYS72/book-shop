# Generated by Django 4.1.3 on 2022-11-30 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=50)),
                ('category', models.TextField(max_length=50)),
                ('price', models.DecimalField(decimal_places=5, max_digits=7)),
                ('published', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]