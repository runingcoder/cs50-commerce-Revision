# Generated by Django 4.1 on 2023-04-24 19:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0006_category_listing"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="category",
            name="listing",
        ),
    ]
