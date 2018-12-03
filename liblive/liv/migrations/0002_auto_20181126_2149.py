# Generated by Django 2.1.3 on 2018-11-26 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('liv', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActualBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('notes', models.TextField()),
                ('key', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='BookFromLibrary',
        ),
        migrations.AlterField(
            model_name='bookfromlivelib',
            name='rating',
            field=models.FloatField(),
        ),
    ]
