# Generated by Django 4.1.7 on 2023-04-10 08:36

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("income", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="income",
            options={"ordering": ("-updated_at",)},
        ),
    ]