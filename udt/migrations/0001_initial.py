# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-30 08:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dispatcher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_type', models.CharField(choices=[('Change', 'Change'), ('Incident', 'Incident'), ('Problem', 'Problem'), ('Other', 'Other')], max_length=10)),
                ('requested_via', models.CharField(choices=[('Change Support', 'Change Support'), ('Incident Support', 'Incident Support'), ('Problem Support', 'Problem Support'), ('Notes', 'Notes'), ('Sametime', 'Sametime'), ('Phone', 'Phone'), ('RTC', 'RTC'), ('Other', 'Other')], max_length=20)),
                ('geo', models.CharField(choices=[('EMEA', 'EMEA'), ('AG', 'AG')], max_length=15)),
                ('filter_by_tool', models.CharField(choices=[('URT', 'URT'), ('ECM', 'ECM'), ('ePolicy', 'ePolicy'), ('CWP', 'CWP'), ('SecInfo', 'SecInfo'), ('Cirats DB2', 'Cirats DB2'), ('Cirats Alps&Germany', 'Cirats Alps&Germany')], max_length=20)),
                ('task', models.CharField(max_length=250)),
                ('slug', models.SlugField(unique_for_date='task_received')),
                ('task_received', models.DateTimeField(default=django.utils.timezone.now)),
                ('link', models.CharField(max_length=500)),
                ('severity', models.CharField(choices=[('Sev 1', 'Sev 1'), ('Sev 2', 'Sev 2'), ('Sev 3', 'Sev 3'), ('Sev 4', 'Sev 4')], max_length=5)),
                ('request_contained', models.PositiveIntegerField(default=1)),
                ('affected_items', models.PositiveIntegerField(default=1)),
                ('subject', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('assign_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='work_orders', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-task_received',),
            },
        ),
    ]
