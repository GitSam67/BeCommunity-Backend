# Generated by Django 4.2.2 on 2023-06-26 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0005_editprofile"),
    ]

    operations = [
        migrations.AlterField(
            model_name="editprofile",
            name="bio",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="editprofile",
            name="dob",
            field=models.DateField(blank=True, null=True),
        ),
    ]
