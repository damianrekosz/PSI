# Generated by Django 2.2.7 on 2019-11-28 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Eksponaty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=200)),
                ('dataProdukcji', models.DateField()),
                ('miejscePochodzenia', models.CharField(max_length=200)),
                ('stanEksponatu', models.CharField(max_length=200)),
                ('czyZarezerwowany', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Pracownicy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwisko', models.CharField(max_length=200)),
                ('imie', models.CharField(max_length=200)),
                ('pesel', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rozmiar', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Wydarzenia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=200)),
                ('eksponaty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='muzeumApp.Eksponaty')),
                ('pracownicy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='muzeumApp.Pracownicy')),
                ('sale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='muzeumApp.Sale')),
            ],
        ),
    ]