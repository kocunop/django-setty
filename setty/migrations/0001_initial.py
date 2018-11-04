# Generated by Django 2.0.3 on 2018-10-25 18:51

from django.db import migrations, models
import picklefield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SettySettings',
            fields=[
                ('name', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('value', picklefield.fields.PickledObjectField(editable=False)),
                ('type', models.CharField(choices=[('bool', 'Bool'), ('dict', 'Dict'), ('float', 'Float'), ('integer', 'Integer'), ('list', 'List'), ('string', 'String')], max_length=8)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Setty Settings',
                'verbose_name_plural': 'Setty Settings',
            },
        ),
    ]
