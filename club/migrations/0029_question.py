# Generated by Django 3.0.2 on 2020-01-09 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0028_member_school_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(help_text='The question.', max_length=400)),
                ('answer', models.CharField(help_text='The question.', max_length=400)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
