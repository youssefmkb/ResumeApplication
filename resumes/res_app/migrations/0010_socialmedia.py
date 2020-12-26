
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('res_app', '0009_auto_20190217_0015'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, help_text='date record created.')),
                ('date_modified', models.DateTimeField(auto_now=True, help_text='date of most recent record modification.')),
                ('media_name', models.CharField(blank=True, help_text='The name of the social media platform (e.g. GitHub)', max_length=200, null=True)),
                ('href', models.URLField(blank=True, help_text='The URL used to connect to this social media profile', null=True)),
                ('icon', models.CharField(blank=True, help_text='The Font Awesome icon code to be applied.', max_length=200, null=True)),
                ('created_by', models.ForeignKey(blank=True, help_text='user who created record.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='SocialMedia_created', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, help_text='user who most recently modified record.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='SocialMedia_modified', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
