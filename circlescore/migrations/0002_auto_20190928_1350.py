# Generated by Django 2.2.5 on 2019-09-28 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('circlescore', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='edit_date',
        ),
        migrations.RemoveField(
            model_name='hikayauser',
            name='edit_date',
        ),
        migrations.RemoveField(
            model_name='historicalcountry',
            name='edit_date',
        ),
        migrations.RemoveField(
            model_name='historicalhikayauser',
            name='edit_date',
        ),
        migrations.RemoveField(
            model_name='historicalworkflowlevel1',
            name='edit_date',
        ),
        migrations.RemoveField(
            model_name='workflowlevel1',
            name='edit_date',
        ),
        migrations.AddField(
            model_name='country',
            name='modified_date',
            field=models.DateTimeField(blank=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='hikayauser',
            name='modified_date',
            field=models.DateTimeField(blank=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='historicalcountry',
            name='modified_date',
            field=models.DateTimeField(blank=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='historicalhikayauser',
            name='modified_date',
            field=models.DateTimeField(blank=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='historicalworkflowlevel1',
            name='modified_date',
            field=models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Modified Date'),
        ),
        migrations.AddField(
            model_name='workflowlevel1',
            name='modified_date',
            field=models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Modified Date'),
        ),
        migrations.AlterField(
            model_name='account',
            name='create_date',
            field=models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Create Date'),
        ),
        migrations.AlterField(
            model_name='account',
            name='modified_date',
            field=models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Modified Date'),
        ),
        migrations.AlterField(
            model_name='accounttype',
            name='create_date',
            field=models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Create Date'),
        ),
        migrations.AlterField(
            model_name='accounttype',
            name='modified_date',
            field=models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Edit Date'),
        ),
        migrations.AlterField(
            model_name='administrativelevel',
            name='create_date',
            field=models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Create Date'),
        ),
        migrations.AlterField(
            model_name='administrativelevel',
            name='modified_date',
            field=models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Modified Date'),
        ),
        migrations.AlterField(
            model_name='approval',
            name='modified_date',
            field=models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Modified Date'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='create_date',
            field=models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Create Date'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='modified_date',
            field=models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Modified Date'),
        ),
        migrations.AlterField(
            model_name='country',
            name='create_date',
            field=models.DateTimeField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='modified_date',
            field=models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Modified Date'),
        ),
        migrations.AlterField(
            model_name='fundingstatus',
            name='create_date',
            field=models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Create Date'),
        ),
        migrations.AlterField(
            model_name='fundingstatus',
            name='modified_date',
            field=models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Modified Date'),
        ),
        migrations.AlterField(
            model_name='hikayauser',
            name='create_date',
            field=models.DateTimeField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='historicalaccount',
            name='create_date',
            field=models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Create Date'),
        ),
        migrations.AlterField(
            model_name='historicalaccount',
            name='modified_date',
            field=models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Modified Date'),
        ),
        migrations.AlterField(
            model_name='historicalaccounttype',
            name='create_date',
            field=models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Create Date'),
        ),
        migrations.AlterField(
            model_name='historicalaccounttype',
            name='modified_date',
            field=models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Edit Date'),
        ),
        migrations.AlterField(
            model_name='historicaladministrativelevel',
            name='create_date',
            field=models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Create Date'),
        ),
        migrations.AlterField(
            model_name='historicaladministrativelevel',
            name='modified_date',
            field=models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Modified Date'),
        ),
        migrations.AlterField(
            model_name='historicalapproval',
            name='modified_date',
            field=models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Modified Date'),
        ),
        migrations.AlterField(
            model_name='historicalcontact',
            name='create_date',
            field=models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Create Date'),
        ),
        migrations.AlterField(
            model_name='historicalcontact',
            name='modified_date',
            field=models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Modified Date'),
        ),
        migrations.AlterField(
            model_name='historicalcountry',
            name='create_date',
            field=models.DateTimeField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='historicaldocument',
            name='modified_date',
            field=models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Modified Date'),
        ),
        migrations.AlterField(
            model_name='historicalfundingstatus',
            name='create_date',
            field=models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Create Date'),
        ),
        migrations.AlterField(
            model_name='historicalfundingstatus',
            name='modified_date',
            field=models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Modified Date'),
        ),
        migrations.AlterField(
            model_name='historicalhikayauser',
            name='create_date',
            field=models.DateTimeField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='historicallocation',
            name='create_date',
            field=models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Create Date'),
        ),
        migrations.AlterField(
            model_name='historicallocation',
            name='modified_date',
            field=models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Modified Date'),
        ),
        migrations.AlterField(
            model_name='historicaloffice',
            name='create_date',
            field=models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Create Date'),
        ),
        migrations.AlterField(
            model_name='historicaloffice',
            name='modified_date',
            field=models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Modified Date'),
        ),
        migrations.AlterField(
            model_name='historicalsector',
            name='create_date',
            field=models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Create Date'),
        ),
        migrations.AlterField(
            model_name='historicalsector',
            name='modified_date',
            field=models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Modified Date'),
        ),
        migrations.AlterField(
            model_name='historicalworkflowlevel1type',
            name='create_date',
            field=models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Create Date'),
        ),
        migrations.AlterField(
            model_name='historicalworkflowlevel1type',
            name='modified_date',
            field=models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Modified Date'),
        ),
        migrations.AlterField(
            model_name='historicalworkflowlevel2',
            name='modified_date',
            field=models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Modified Date'),
        ),
        migrations.AlterField(
            model_name='historicalworkflowlevel2plan',
            name='modified_date',
            field=models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Modified Date'),
        ),
        migrations.AlterField(
            model_name='historicalworkflowlevel2type',
            name='create_date',
            field=models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Create Date'),
        ),
        migrations.AlterField(
            model_name='historicalworkflowlevel2type',
            name='modified_date',
            field=models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Modified Date'),
        ),
        migrations.AlterField(
            model_name='historicalworkflowstatus',
            name='modified_date',
            field=models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Modified Date'),
        ),
        migrations.AlterField(
            model_name='location',
            name='create_date',
            field=models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Create Date'),
        ),
        migrations.AlterField(
            model_name='location',
            name='modified_date',
            field=models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Modified Date'),
        ),
        migrations.AlterField(
            model_name='office',
            name='create_date',
            field=models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Create Date'),
        ),
        migrations.AlterField(
            model_name='office',
            name='modified_date',
            field=models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Modified Date'),
        ),
        migrations.AlterField(
            model_name='sector',
            name='create_date',
            field=models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Create Date'),
        ),
        migrations.AlterField(
            model_name='sector',
            name='modified_date',
            field=models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Modified Date'),
        ),
        migrations.AlterField(
            model_name='workflowlevel1type',
            name='create_date',
            field=models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Create Date'),
        ),
        migrations.AlterField(
            model_name='workflowlevel1type',
            name='modified_date',
            field=models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Modified Date'),
        ),
        migrations.AlterField(
            model_name='workflowlevel2',
            name='modified_date',
            field=models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Modified Date'),
        ),
        migrations.AlterField(
            model_name='workflowlevel2plan',
            name='modified_date',
            field=models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Modified Date'),
        ),
        migrations.AlterField(
            model_name='workflowlevel2type',
            name='create_date',
            field=models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Create Date'),
        ),
        migrations.AlterField(
            model_name='workflowlevel2type',
            name='modified_date',
            field=models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Modified Date'),
        ),
        migrations.AlterField(
            model_name='workflowstatus',
            name='modified_date',
            field=models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Modified Date'),
        ),
    ]
