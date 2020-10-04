# Generated by Django 3.1.2 on 2020-10-02 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('networkscanners', '0011_auto_20201002_1855'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nessus_scan_db',
            old_name='SEVERITY_HIGH',
            new_name='total_high',
        ),
        migrations.RenameField(
            model_name='nessus_scan_db',
            old_name='SEVERITY_LOW',
            new_name='total_low',
        ),
        migrations.RenameField(
            model_name='nessus_scan_db',
            old_name='SEVERITY_MEDIUM',
            new_name='total_medium',
        ),
        migrations.RemoveField(
            model_name='nessus_scan_db',
            name='critical_total',
        ),
        migrations.RemoveField(
            model_name='nessus_scan_db',
            name='high_total',
        ),
        migrations.RemoveField(
            model_name='nessus_scan_db',
            name='info_total',
        ),
        migrations.RemoveField(
            model_name='nessus_scan_db',
            name='low_total',
        ),
        migrations.RemoveField(
            model_name='nessus_scan_db',
            name='medium_total',
        ),
        migrations.RemoveField(
            model_name='nessus_scan_db',
            name='total_vul',
        ),
        migrations.RemoveField(
            model_name='nessus_scan_results_db',
            name='vul_id',
        ),
    ]
