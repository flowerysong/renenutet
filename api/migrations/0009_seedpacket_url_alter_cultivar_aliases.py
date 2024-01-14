# Generated by Django 4.2.4 on 2024-01-14 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_planting_options_alter_seedpacket_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='seedpacket',
            name='url',
            field=models.URLField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='cultivar',
            name='aliases',
            field=models.JSONField(blank=True, default=list),
        ),
    ]
