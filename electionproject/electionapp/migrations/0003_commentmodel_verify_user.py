# Generated by Django 4.1.7 on 2023-04-19 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electionapp', '0002_alter_commentmodel_pollingstation_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentmodel',
            name='verify_user',
            field=models.CharField(choices=[('Verified', 'Verified'), ('NotVerified', 'NotVerified')], default=1, max_length=100),
            preserve_default=False,
        ),
    ]
