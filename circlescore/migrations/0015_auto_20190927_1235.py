# Generated by Django 2.2.4 on 2019-09-27 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('circlescore', '0014_auto_20190927_0908'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='organization_type',
            new_name='account_type',
        ),
        migrations.RenameField(
            model_name='account',
            old_name='parent_organization',
            new_name='parent_account',
        ),
        migrations.RenameField(
            model_name='accountsubtype',
            old_name='type',
            new_name='account_type',
        ),
        migrations.RenameField(
            model_name='historicalaccount',
            old_name='organization_type',
            new_name='account_type',
        ),
        migrations.RenameField(
            model_name='historicalaccount',
            old_name='parent_organization',
            new_name='parent_account',
        ),
        migrations.RenameField(
            model_name='historicalaccountsubtype',
            old_name='type',
            new_name='account_type',
        ),
        migrations.AddField(
            model_name='account',
            name='account_sub_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='circlescore.AccountSubType'),
        ),
        migrations.AddField(
            model_name='historicalaccount',
            name='account_sub_type',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='circlescore.AccountSubType'),
        ),
        migrations.AlterField(
            model_name='account',
            name='full_name',
            field=models.CharField(max_length=135, verbose_name="Account's Full Name"),
        ),
        migrations.AlterField(
            model_name='account',
            name='link_to_description_relationship',
            field=models.CharField(blank=True, max_length=165, null=True, verbose_name='Link to Description of Relationship'),
        ),
        migrations.AlterField(
            model_name='account',
            name='short_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Account Short Name'),
        ),
        migrations.AlterField(
            model_name='account',
            name='url',
            field=models.CharField(blank=True, max_length=165, null=True, verbose_name="Account's Website URL"),
        ),
        migrations.AlterField(
            model_name='historicalaccount',
            name='full_name',
            field=models.CharField(max_length=135, verbose_name="Account's Full Name"),
        ),
        migrations.AlterField(
            model_name='historicalaccount',
            name='link_to_description_relationship',
            field=models.CharField(blank=True, max_length=165, null=True, verbose_name='Link to Description of Relationship'),
        ),
        migrations.AlterField(
            model_name='historicalaccount',
            name='short_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Account Short Name'),
        ),
        migrations.AlterField(
            model_name='historicalaccount',
            name='url',
            field=models.CharField(blank=True, max_length=165, null=True, verbose_name="Account's Website URL"),
        ),
    ]