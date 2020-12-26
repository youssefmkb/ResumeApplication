
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('res_app', '0012_auto_20190217_0051'),
    ]

    operations = [
        migrations.CreateModel(
            name='EducationHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, help_text='date record created.')),
                ('date_modified', models.DateTimeField(auto_now=True, help_text='date of most recent record modification.')),
                ('institution', models.CharField(blank=True, help_text='The name of the educational institution', max_length=200, null=True)),
                ('start_date', models.DateField(blank=True, help_text='The start date for this education history', null=True)),
                ('end_date', models.DateField(blank=True, help_text='The end date for this education history', null=True)),
                ('graduated', models.BooleanField(default=False, help_text='Whether or not a person graduated from this particular institution')),
                ('degree_attained', models.CharField(blank=True, help_text='The degree (if any) attained at this institution', max_length=100, null=True)),
                ('focus', models.CharField(blank=True, help_text='The focus (e.g. major, thesis, etc.) of this academic history', max_length=200, null=True)),
                ('created_by', models.ForeignKey(blank=True, help_text='user who created record.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Eduction_created', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, help_text='user who most recently modified record.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Eduction_modified', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterModelOptions(
            name='socialmedia',
            options={'verbose_name_plural': 'Social Media'},
        ),
        migrations.AddField(
            model_name='ksa',
            name='type',
            field=models.CharField(blank=True, choices=[('sk', 'Skill'), ('tc', 'Technology')], help_text='The type of knowledge, skill, or ability this record represents', max_length=2, null=True),
        ),
    ]
