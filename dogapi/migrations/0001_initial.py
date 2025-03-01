# Generated by Django 5.1.1 on 2024-10-12 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('size', models.CharField(max_length=100, verbose_name=[('Tiny', 'Tiny'), ('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large')])),
                ('friendliness', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('trainability', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('sheddingamount', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('exerciseneeds', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
            ],
        ),
    ]
