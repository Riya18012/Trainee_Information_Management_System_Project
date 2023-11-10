# Generated by Django 4.2.3 on 2023-08-28 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("trainee_mgt", "0002_remove_course_end_date_remove_course_start_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="enrollment",
            name="training_period",
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name="trainee",
            name="course",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="trainee_mgt.course",
            ),
        ),
        migrations.AddField(
            model_name="trainer",
            name="designation",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="trainer",
            name="specialization",
            field=models.CharField(max_length=100, null=True),
        ),
    ]
