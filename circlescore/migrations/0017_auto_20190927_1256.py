# Generated by Django 2.2.4 on 2019-09-27 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('circlescore', '0016_auto_20190927_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountsubtype',
            name='account_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='circlescore.AccountType', verbose_name='Account Type'),
        ),
    ]
