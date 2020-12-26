
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('res_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactinfo',
            options={'verbose_name_plural': 'Contact Info'},
        ),
        migrations.AlterModelOptions(
            name='ksa',
            options={'verbose_name_plural': 'KSAs'},
        ),
        migrations.AddField(
            model_name='resume',
            name='name',
            field=models.CharField(blank=True, help_text='A simple name to identify this resume', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='employment',
            name='end_date',
            field=models.DateField(help_text='The approximate end date for this employment'),
        ),
        migrations.AlterField(
            model_name='employment',
            name='start_date',
            field=models.DateField(help_text='The approximate start date for this employment'),
        ),
    ]
