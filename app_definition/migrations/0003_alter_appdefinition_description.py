# Generated by Django 4.2.1 on 2023-06-03 20:45

from django.db import migrations
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app_definition', '0002_alter_appdefinition_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appdefinition',
            name='description',
            field=mdeditor.fields.MDTextField(blank=True, null=True),
        ),
    ]