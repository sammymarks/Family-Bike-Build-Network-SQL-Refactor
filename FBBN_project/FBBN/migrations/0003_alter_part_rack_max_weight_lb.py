# Generated by Django 5.0.2 on 2024-02-12 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FBBN', '0002_part_trailer_is_stroller'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part_rack',
            name='max_weight_lb',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
