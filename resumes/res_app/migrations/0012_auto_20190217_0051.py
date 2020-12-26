
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('res_app', '0011_contactinfo_social_media'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactinfo',
            name='social_media',
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='social_media',
            field=models.ManyToManyField(to='res_app.SocialMedia'),
        ),
    ]
