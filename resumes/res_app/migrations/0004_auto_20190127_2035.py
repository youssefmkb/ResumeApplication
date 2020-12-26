
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('res_app', '0003_employment_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employment',
            name='end_date',
            field=models.DateField(blank=True, help_text='The approximate end date for this employment', null=True),
        ),
    ]
