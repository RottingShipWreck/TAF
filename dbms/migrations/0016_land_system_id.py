# Generated by Django 2.2.2 on 2019-06-26 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbms', '0015_auto_20190626_0116'),
    ]

    operations = [
        migrations.AddField(
            model_name='land',
            name='system_id',
            field=models.CharField(default='None', max_length=10),
        ),
    ]
