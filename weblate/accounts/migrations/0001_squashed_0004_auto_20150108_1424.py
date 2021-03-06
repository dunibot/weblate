# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-27 17:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('accounts', '0001_initial'), ('accounts', '0002_auto_20140923_1543'), ('accounts', '0003_auto_20141104_1159'), ('accounts', '0004_auto_20150108_1424')]

    initial = True

    dependencies = [
        ('social_django', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trans', '0001_initial'),
        ('lang', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(choices=[(b'az', 'Az\u0259rbaycan'), (b'be', '\u0411\u0435\u043b\u0430\u0440\u0443\u0441\u043a\u0430\u044f'), (b'be@latin', 'Bie\u0142aruskaja'), (b'br', 'Brezhoneg'), (b'ca', 'Catal\xe0'), (b'cs', '\u010ce\u0161tina'), (b'da', 'Dansk'), (b'de', 'Deutsch'), (b'en', 'English'), (b'el', '\u0395\u03bb\u03bb\u03b7\u03bd\u03b9\u03ba\u03ac'), (b'es', 'Espa\xf1ol'), (b'fi', 'Suomi'), (b'fr', 'Fran\xe7ais'), (b'fy', 'Frysk'), (b'gl', 'Galego'), (b'he', '\u05e2\u05d1\u05e8\u05d9\u05ea'), (b'hu', 'Magyar'), (b'id', b'Indonesia'), (b'ja', '\u65e5\u672c\u8a9e'), (b'ko', '\ud55c\uad6d\uc5b4'), (b'ksh', 'K\xf6lsch'), (b'nl', 'Nederlands'), (b'pl', 'Polski'), (b'pt', 'Portugu\xeas'), (b'pt_BR', 'Portugu\xeas brasileiro'), (b'ru', '\u0420\u0443\u0441\u0441\u043a\u0438\u0439'), (b'sk', 'Sloven\u010dina'), (b'sl', 'Sloven\u0161\u010dina'), (b'sv', 'Svenska'), (b'tr', 'T\xfcrk\xe7e'), (b'uk', '\u0423\u043a\u0440\u0430\u0457\u043d\u0441\u044c\u043a\u0430'), (b'zh_CN', '\u7b80\u4f53\u5b57'), (b'zh_TW', '\u6b63\u9ad4\u5b57')], max_length=10, verbose_name='Interface Language')),
                ('suggested', models.IntegerField(db_index=True, default=0)),
                ('translated', models.IntegerField(db_index=True, default=0)),
                ('subscribe_any_translation', models.BooleanField(default=False, verbose_name='Notification on any translation')),
                ('subscribe_new_string', models.BooleanField(default=False, verbose_name='Notification on new string to translate')),
                ('subscribe_new_suggestion', models.BooleanField(default=False, verbose_name='Notification on new suggestion')),
                ('subscribe_new_contributor', models.BooleanField(default=False, verbose_name='Notification on new contributor')),
                ('subscribe_new_comment', models.BooleanField(default=False, verbose_name='Notification on new comment')),
                ('subscribe_merge_failure', models.BooleanField(default=False, verbose_name='Notification on merge failure')),
                ('subscribe_new_language', models.BooleanField(default=False, verbose_name='Notification on new language request')),
                ('languages', models.ManyToManyField(blank=True, to='lang.Language', verbose_name='Languages')),
                ('secondary_languages', models.ManyToManyField(blank=True, related_name=b'secondary_profile_set', to='lang.Language', verbose_name='Secondary languages')),
                ('subscriptions', models.ManyToManyField(blank=True, to='trans.Project', verbose_name='Subscribed projects')),
                ('user', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VerifiedEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('social', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='social_django.UserSocialAuth')),
            ],
        ),
    ]
