
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('res_app', '0004_auto_20190127_2035'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, help_text='date record created.')),
                ('date_modified', models.DateTimeField(auto_now=True, help_text='date of most recent record modification.')),
                ('name', models.CharField(blank=True, help_text='The brief name of this projects', max_length=200, null=True)),
                ('url', models.URLField(blank=True, help_text='A URL to point people towards this project', null=True)),
                ('description', models.TextField(help_text='A description of this project')),
                ('created_by', models.ForeignKey(blank=True, help_text='user who created record.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Project_created', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, help_text='user who most recently modified record.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Project_modified', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='resume',
            name='projects',
            field=models.ManyToManyField(to='res_app.Project'),
        ),
    ]
