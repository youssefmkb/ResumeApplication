
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('res_app', '0002_auto_20190127_2008'),
    ]

    operations = [
        migrations.AddField(
            model_name='employment',
            name='position',
            field=models.CharField(blank=True, help_text='The name of the position held at this employer', max_length=200, null=True),
        ),
    ]
