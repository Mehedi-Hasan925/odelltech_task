# Generated by Django 3.2.9 on 2021-11-21 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_user_info', '0002_user_info_division'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Districts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='user_info',
            name='zilla',
        ),
        migrations.CreateModel(
            name='Upazilla',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thana', to='app_user_info.districts')),
            ],
        ),
        migrations.CreateModel(
            name='Divisions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='divisions', to='app_user_info.country')),
            ],
        ),
        migrations.AddField(
            model_name='districts',
            name='division',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='zila', to='app_user_info.divisions'),
        ),
        migrations.AddField(
            model_name='user_info',
            name='District',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dstrct', to='app_user_info.districts'),
        ),
        migrations.AlterField(
            model_name='user_info',
            name='Division',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dvsn', to='app_user_info.divisions'),
        ),
        migrations.AlterField(
            model_name='user_info',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cntry', to='app_user_info.country'),
        ),
        migrations.AlterField(
            model_name='user_info',
            name='upazilla',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='upzla', to='app_user_info.upazilla'),
        ),
    ]
