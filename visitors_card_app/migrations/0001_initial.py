# Generated by Django 3.2 on 2022-06-16 05:18

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='役職名')),
            ],
            options={
                'verbose_name': '役職',
                'verbose_name_plural': '役職',
                'db_table': '役職',
            },
        ),
        migrations.CreateModel(
            name='Visitors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='日付')),
                ('time', models.TimeField(verbose_name='来室時刻')),
                ('company_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='会社名')),
                ('visitor_name', models.CharField(max_length=25, verbose_name='お名前')),
                ('temperature', models.FloatField(verbose_name='検温')),
                ('accompany1_name', models.CharField(blank=True, max_length=25, null=True, verbose_name='同行者1お名前')),
                ('accompany1_temp', models.FloatField(blank=True, null=True, verbose_name='同行者1検温')),
                ('accompany2_name', models.CharField(blank=True, max_length=25, null=True, verbose_name='同行者2お名前')),
                ('accompany2_temp', models.FloatField(blank=True, null=True, verbose_name='同行者2検温')),
                ('accompany3_name', models.CharField(blank=True, max_length=25, null=True, verbose_name='同行者3お名前')),
                ('accompany3_temp', models.FloatField(blank=True, null=True, verbose_name='同行者3検温')),
                ('position', models.CharField(blank=True, max_length=25, null=True, verbose_name='役職')),
                ('interviewer', models.CharField(blank=True, max_length=25, null=True, verbose_name='担当者')),
                ('content', models.TextField(blank=True, null=True, verbose_name='ご用件')),
                ('is_contacted', models.BooleanField(default=False, help_text='コンタクトしたらTrue')),
            ],
            options={
                'verbose_name': '来訪者履歴',
                'verbose_name_plural': '来訪者履歴',
                'db_table': 'visitors_history',
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=25, null=True, verbose_name='氏名')),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='visitors_card_app.post')),
            ],
            options={
                'verbose_name': '社員メンバー',
                'verbose_name_plural': '社員メンバー',
                'db_table': '社員メンバー',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField(blank=True, null=True, verbose_name='退室時刻')),
                ('contents', models.TextField(blank=True, null=True, verbose_name='内容')),
                ('contact', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='visitors_card_app.visitors', verbose_name='来訪者履歴')),
                ('interviewer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='visitors_card_app.member', verbose_name='担当者')),
            ],
            options={
                'verbose_name': 'コンタクト履歴',
                'verbose_name_plural': 'コンタクト履歴',
                'db_table': 'contact_history',
            },
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name_plural': 'CustomUser',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
