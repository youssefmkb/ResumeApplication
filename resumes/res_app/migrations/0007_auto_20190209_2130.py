
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('res_app', '0006_auto_20190203_1733'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='template_name',
            field=models.CharField(blank=True, help_text='The string identifying the template to be used to render this resume.', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='projects',
            field=models.ManyToManyField(to='res_app.Project'),
        ),
    ]
