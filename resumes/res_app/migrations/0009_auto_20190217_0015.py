
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('res_app', '0008_resume_summary'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employment',
            options={'ordering': ['-start_date']},
        ),
        migrations.AddField(
            model_name='resume',
            name='headline',
            field=models.CharField(blank=True, help_text='The title to appear under your name', max_length=200, null=True),
        ),
    ]
