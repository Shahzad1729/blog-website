# Generated by Django 2.0.5 on 2022-07-01 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20220617_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='imageURL',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]
