# Generated by Django 2.0.3 on 2018-03-30 04:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('deals', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dealvote',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deal_votes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='deal',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='deals', to='deals.Category'),
        ),
        migrations.AddField(
            model_name='deal',
            name='created_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='deals', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='deal',
            name='edited_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='deal',
            name='vendor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='deals', to='deals.Vendor'),
        ),
        migrations.AddField(
            model_name='commentvote',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='deals.Comment'),
        ),
        migrations.AddField(
            model_name='commentvote',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_votes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='created_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='deal',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='deals.Deal'),
        ),
        migrations.AddField(
            model_name='comment',
            name='edited_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='deals.Comment'),
        ),
        migrations.AddField(
            model_name='category',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='deals.Category'),
        ),
        migrations.AlterUniqueTogether(
            name='dealvote',
            unique_together={('deal', 'user')},
        ),
        migrations.AlterUniqueTogether(
            name='commentvote',
            unique_together={('comment', 'user')},
        ),
    ]
