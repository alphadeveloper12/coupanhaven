# Generated by Django 4.2.4 on 2023-09-05 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_store_deeplink'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='description',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]