# Generated by Django 4.1.3 on 2023-02-27 23:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("rmc", "0003_alter_degreeprogramme_programme_courses"),
    ]

    operations = [
        migrations.AlterField(
            model_name="degreeprogramme",
            name="name",
            field=models.CharField(
                max_length=32, unique=True, verbose_name="Degree programme name"
            ),
        ),
        migrations.AlterField(
            model_name="student",
            name="degree_programme",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="rmc.degreeprogramme",
                to_field="name",
            ),
        ),
    ]