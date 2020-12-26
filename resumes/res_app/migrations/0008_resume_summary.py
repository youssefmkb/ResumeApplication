
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('res_app', '0007_auto_20190209_2130'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='summary',
            field=models.TextField(blank=True, help_text='A personal summary or general description of an employment goal to top the resume.', null=True),
        ),
    ]
