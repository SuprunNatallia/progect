# Generated by Django 4.1.7 on 2023-04-11 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Specialists',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='uploads')),
                ('name', models.CharField(max_length=250)),
                ('position', models.CharField(max_length=250)),
                ('additional', models.CharField(max_length=250)),
            ],
        ),
        migrations.AlterField(
            model_name='cosmetolog',
            name='price',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='cosmetolog',
            name='service',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='massages',
            name='price',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='massages',
            name='service',
            field=models.CharField(max_length=250),
        ),
    ]
