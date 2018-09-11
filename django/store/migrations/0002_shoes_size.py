# Generated by Django 2.1.1 on 2018-09-11 19:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shoes_size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=15)),
                ('stock', models.BooleanField()),
                ('shoes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Shoes')),
            ],
        ),
    ]
