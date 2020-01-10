# Generated by Django 3.0.2 on 2020-01-10 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0033_member_verified'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='verification_code',
            field=models.CharField(blank=True, help_text="The randomly generated code sent to the user's school email to verify it.", max_length=100, null=True),
        ),
    ]