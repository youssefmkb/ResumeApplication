
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, help_text='date record created.')),
                ('date_modified', models.DateTimeField(auto_now=True, help_text='date of most recent record modification.')),
                ('street_1', models.CharField(blank=True, help_text='First line in a street address', max_length=100, null=True)),
                ('street_2', models.CharField(blank=True, help_text='Second line for street address', max_length=100, null=True)),
                ('street_3', models.CharField(blank=True, help_text='Third line in street address', max_length=100, null=True)),
                ('city', models.CharField(blank=True, help_text='City', max_length=100, null=True)),
                ('state', models.CharField(blank=True, max_length=2, null=True)),
                ('zip_code', models.CharField(blank=True, max_length=15, null=True)),
                ('created_by', models.ForeignKey(blank=True, help_text='user who created record.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Address_created', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, help_text='user who most recently modified record.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Address_modified', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, help_text='date record created.')),
                ('date_modified', models.DateTimeField(auto_now=True, help_text='date of most recent record modification.')),
                ('email', models.EmailField(blank=True, help_text='Enter a valid email address', max_length=254, null=True)),
                ('address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='res_app.Address')),
                ('created_by', models.ForeignKey(blank=True, help_text='user who created record.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ContactInfo_created', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, help_text='user who most recently modified record.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ContactInfo_modified', to=settings.AUTH_USER_MODEL)),
                ('person', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Employment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, help_text='date record created.')),
                ('date_modified', models.DateTimeField(auto_now=True, help_text='date of most recent record modification.')),
                ('employer', models.CharField(blank=True, help_text='The name of the employer', max_length=200, null=True)),
                ('start_date', models.DateTimeField(help_text='The approximate start date for this employment')),
                ('end_date', models.DateTimeField(help_text='The approximate end date for this employment')),
                ('description', models.TextField(help_text='A description of this employment')),
                ('created_by', models.ForeignKey(blank=True, help_text='user who created record.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Employment_created', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='KSA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, help_text='date record created.')),
                ('date_modified', models.DateTimeField(auto_now=True, help_text='date of most recent record modification.')),
                ('name', models.CharField(blank=True, help_text='The short name for this KSA', max_length=100, null=True)),
                ('years', models.FloatField(default=0, help_text='The number of years experience with this KSA')),
                ('description', models.TextField(help_text='A description of this particular KSA')),
                ('created_by', models.ForeignKey(blank=True, help_text='user who created record.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='KSA_created', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, help_text='user who most recently modified record.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='KSA_modified', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, help_text='date record created.')),
                ('date_modified', models.DateTimeField(auto_now=True, help_text='date of most recent record modification.')),
                ('phone_number', models.CharField(blank=True, help_text='Enter your phone number', max_length=100, null=True)),
                ('type', models.CharField(blank=True, choices=[('h', 'Home'), ('w', 'Work'), ('m', 'Mobile')], help_text='The type of phone number represented by this record', max_length=1, null=True)),
                ('created_by', models.ForeignKey(blank=True, help_text='user who created record.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='PhoneNumber_created', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, help_text='user who most recently modified record.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='PhoneNumber_modified', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, help_text='date record created.')),
                ('date_modified', models.DateTimeField(auto_now=True, help_text='date of most recent record modification.')),
                ('style_class', models.CharField(blank=True, help_text='The CSS style class to be applied when rendering this resume', max_length=100, null=True)),
                ('css_file_name', models.CharField(blank=True, help_text='The specific css file that will be loaded for this resume', max_length=100, null=True)),
                ('created_by', models.ForeignKey(blank=True, help_text='user who created record.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Resume_created', to=settings.AUTH_USER_MODEL)),
                ('employment_histories', models.ManyToManyField(to='res_app.Employment')),
                ('ksas', models.ManyToManyField(to='res_app.KSA')),
                ('modified_by', models.ForeignKey(blank=True, help_text='user who most recently modified record.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Resume_modified', to=settings.AUTH_USER_MODEL)),
                ('person', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='employment',
            name='ksas',
            field=models.ManyToManyField(help_text='The Knowledge, Skills, and Abilities used in this employment', to='res_app.KSA', verbose_name="KSA's"),
        ),
        migrations.AddField(
            model_name='employment',
            name='modified_by',
            field=models.ForeignKey(blank=True, help_text='user who most recently modified record.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Employment_modified', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='phone_numbers',
            field=models.ManyToManyField(to='res_app.PhoneNumber'),
        ),
    ]
