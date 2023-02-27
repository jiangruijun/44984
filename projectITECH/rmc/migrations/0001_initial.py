# Generated by Django 4.1.3 on 2023-02-27 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=64, verbose_name="Name")),
            ],
        ),
        migrations.CreateModel(
            name="Degree",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=32, verbose_name="Name")),
                ("password", models.CharField(max_length=64, verbose_name="Password")),
                (
                    "gender",
                    models.SmallIntegerField(
                        choices=[(1, "Male"), (2, "Female")], verbose_name="Gender"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DegreeProgramme",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=32, verbose_name="Degree programme name"
                    ),
                ),
                (
                    "level",
                    models.SmallIntegerField(
                        choices=[(1, "Undergraduate"), (2, "Postgraduate")],
                        verbose_name="Level",
                    ),
                ),
                (
                    "programme_courses",
                    models.ManyToManyField(
                        related_name="programme_courses", to="rmc.course"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=32, verbose_name="Name")),
                ("password", models.CharField(max_length=64, verbose_name="Password")),
                (
                    "gender",
                    models.SmallIntegerField(
                        choices=[(1, "Male"), (2, "Female")], verbose_name="Gender"
                    ),
                ),
                ("age", models.IntegerField(verbose_name="Age")),
                ("entry_date", models.DateField(verbose_name="Date of entry")),
                (
                    "degree_programme",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="rmc.degreeprogramme",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CourseReview",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("overall_score", models.IntegerField(verbose_name="Overall score")),
                ("easiness_score", models.IntegerField(verbose_name="Easiness score")),
                ("interest_score", models.IntegerField(verbose_name="Interest score")),
                (
                    "usefulness_score",
                    models.IntegerField(verbose_name="Usefulness score"),
                ),
                ("teaching_score", models.IntegerField(verbose_name="Teaching score")),
                ("comment", models.CharField(default="", max_length=300)),
                (
                    "course_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="rmc.course"
                    ),
                ),
                (
                    "student_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="rmc.student"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="course",
            name="associated_degree_programme",
            field=models.ManyToManyField(
                related_name="associated_degree_programme", to="rmc.degreeprogramme"
            ),
        ),
    ]
