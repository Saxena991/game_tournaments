# Generated by Django 4.2.7 on 2023-11-28 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tournament_Name', models.CharField(max_length=150)),
                ('Game_Name', models.CharField(max_length=150)),
                ('Tournament_Entry_Fees', models.IntegerField()),
                ('Prize_Pool_in_Rupees', models.IntegerField()),
                ('Registration_STARTS_ON', models.DateTimeField()),
                ('Registration_ENDS_ON', models.DateTimeField()),
                ('Tournament_STARTS_ON', models.DateTimeField()),
                ('Tournament_ENDS_ON', models.DateTimeField()),
                ('Tournament_Description', models.TextField(verbose_name=255)),
                ('Streaming_On_channel_name', models.CharField(max_length=150)),
                ('Tournament_Image', models.ImageField(upload_to='images')),
                ('Game_Rules_and_Regulations', models.TextField(verbose_name=255)),
            ],
        ),
    ]
