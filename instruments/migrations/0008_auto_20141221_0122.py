# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instruments', '0007_norwegian_wg'),
    ]

    operations = [
        migrations.AddField(
            model_name='spanish_ws',
            name='item_prsubes',
            field=models.CharField(max_length=20, null=True, choices=[('produces', 'produces')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spanish_ws',
            name='item_cmplx37',
            field=models.CharField(max_length=20, null=True, choices=[('simple', 'simple'), ('complex', 'complex')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spanish_ws',
            name='item_cmplx10',
            field=models.CharField(max_length=20, null=True, choices=[('simple', 'simple'), ('complex', 'complex')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spanish_ws',
            name='item_prcome',
            field=models.CharField(max_length=20, null=True, choices=[('produces', 'produces')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spanish_ws',
            name='item_cmplx14',
            field=models.CharField(max_length=20, null=True, choices=[('simple', 'simple'), ('complex', 'complex')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spanish_ws',
            name='item_cmplx11',
            field=models.CharField(max_length=20, null=True, choices=[('simple', 'simple'), ('complex', 'complex')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spanish_ws',
            name='item_isubete',
            field=models.CharField(max_length=20, null=True, choices=[('produces', 'produces')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spanish_ws',
            name='item_cmplx12',
            field=models.CharField(max_length=20, null=True, choices=[('simple', 'simple'), ('complex', 'complex')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spanish_ws',
            name='item_prcomes',
            field=models.CharField(max_length=20, null=True, choices=[('produces', 'produces')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spanish_ws',
            name='item_cmplx13',
            field=models.CharField(max_length=20, null=True, choices=[('simple', 'simple'), ('complex', 'complex')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spanish_ws',
            name='item_cmplx09',
            field=models.CharField(max_length=20, null=True, choices=[('simple', 'simple'), ('complex', 'complex')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spanish_ws',
            name='item_cmplx25',
            field=models.CharField(max_length=20, null=True, choices=[('simple', 'simple'), ('complex', 'complex')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spanish_ws',
            name='item_cmplx08',
            field=models.CharField(max_length=20, null=True, choices=[('simple', 'simple'), ('complex', 'complex')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spanish_ws',
            name='item_pasubio',
            field=models.CharField(max_length=20, null=True, choices=[('produces', 'produces')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spanish_ws',
            name='item_prcomems',
            field=models.CharField(max_length=20, null=True, choices=[('produces', 'produces')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spanish_ws',
            name='item_cmplx05',
            field=models.CharField(max_length=20, null=True, choices=[('simple', 'simple'), ('complex', 'complex')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spanish_ws',
            name='item_cmplx35',
            field=models.CharField(max_length=20, null=True, choices=[('simple', 'simple'), ('complex', 'complex')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spanish_ws',
            name='item_cmplx07',
            field=models.CharField(max_length=20, null=True, choices=[('simple', 'simple'), ('complex', 'complex')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spanish_ws',
            name='item_prsubims',
            field=models.CharField(max_length=20, null=True, choices=[('produces', 'produces')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spanish_ws',
            name='item_pacomio',
            field=models.CharField(max_length=20, null=True, choices=[('produces', 'produces')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spanish_ws',
            name='item_paacabe',
            field=models.CharField(max_length=20, null=True, choices=[('produces', 'produces')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spanish_ws',
            name='item_cmplx06',
            field=models.CharField(max_length=20, null=True, choices=[('simple', 'simple'), ('complex', 'complex')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spanish_ws',
            name='item_cmplx36',
            field=models.CharField(max_length=20, null=True, choices=[('simple', 'simple'), ('complex', 'complex')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spanish_ws',
            name='item_iacabate',
            field=models.CharField(max_length=20, null=True, choices=[('produces', 'produces')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spanish_ws',
            name='item_cmplx23',
            field=models.CharField(max_length=20, null=True, choices=[('simple', 'simple'), ('complex', 'complex')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spanish_ws',
            name='item_pacomi',
            field=models.CharField(max_length=20, null=True, choices=[('produces', 'produces')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spanish_ws',
            name='item_cmplx17',
            field=models.CharField(max_length=20, null=True, choices=[('simple', 'simple'), ('complex', 'complex')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spanish_ws',
            name='item_cmplx04',
            field=models.CharField(max_length=20, null=True, choices=[('simple', 'simple'), ('complex', 'complex')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spanish_ws',
            name='item_cmplx34',
            field=models.CharField(max_length=20, null=True, choices=[('simple', 'simple'), ('complex', 'complex')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spanish_ws',
            name='item_prcomo',
            field=models.CharField(max_length=20, null=True, choices=[('produces', 'produces')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spanish_ws',
            name='item_iacaba',
            field=models.CharField(max_length=20, null=True, choices=[('produces', 'produces')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spanish_ws',
            name='item_cmplx03',
            field=models.CharField(max_length=20, null=True, choices=[('simple', 'simple'), ('complex', 'complex')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spanish_ws',
            name='item_prsubo',
            field=models.CharField(max_length=20, null=True, choices=[('produces', 'produces')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spanish_ws',
            name='item_cmplx33',
            field=models.CharField(max_length=20, null=True, choices=[('simple', 'simple'), ('complex', 'complex')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spanish_ws',
            name='item_pracaba',
            field=models.CharField(max_length=20, null=True, choices=[('produces', 'produces')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spanish_ws',
            name='item_cmplx24',
            field=models.CharField(max_length=20, null=True, choices=[('simple', 'simple'), ('complex', 'complex')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spanish_ws',
            name='item_cmplx18',
            field=models.CharField(max_length=20, null=True, choices=[('simple', 'simple'), ('complex', 'complex')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spanish_ws',
            name='item_cmplx02',
            field=models.CharField(max_length=20, null=True, choices=[('simple', 'simple'), ('complex', 'complex')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spanish_ws',
            name='item_cmplx27',
            field=models.CharField(max_length=20, null=True, choices=[('simple', 'simple'), ('complex', 'complex')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spanish_ws',
            name='item_pracabms',
            field=models.CharField(max_length=20, null=True, choices=[('produces', 'produces')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spanish_ws',
            name='item_cmplx01',
            field=models.CharField(max_length=20, null=True, choices=[('simple', 'simple'), ('complex', 'complex')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spanish_ws',
            name='item_cmplx32',
            field=models.CharField(max_length=20, null=True, choices=[('simple', 'simple'), ('complex', 'complex')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spanish_ws',
            name='item_isube',
            field=models.CharField(max_length=20, null=True, choices=[('produces', 'produces')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spanish_ws',
            name='item_paacabo',
            field=models.CharField(max_length=20, null=True, choices=[('produces', 'produces')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spanish_ws',
            name='item_cmplx26',
            field=models.CharField(max_length=20, null=True, choices=[('simple', 'simple'), ('complex', 'complex')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spanish_ws',
            name='item_cmplx30',
            field=models.CharField(max_length=20, null=True, choices=[('simple', 'simple'), ('complex', 'complex')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spanish_ws',
            name='item_cmplx31',
            field=models.CharField(max_length=20, null=True, choices=[('simple', 'simple'), ('complex', 'complex')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spanish_ws',
            name='item_scombine',
            field=models.CharField(max_length=20, null=True, choices=[('yes', 'yes'), ('no', 'no')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spanish_ws',
            name='item_icomete',
            field=models.CharField(max_length=20, null=True, choices=[('produces', 'produces')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spanish_ws',
            name='item_pracabo',
            field=models.CharField(max_length=20, null=True, choices=[('produces', 'produces')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spanish_ws',
            name='item_pracabas',
            field=models.CharField(max_length=20, null=True, choices=[('produces', 'produces')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spanish_ws',
            name='item_cmplx15',
            field=models.CharField(max_length=20, null=True, choices=[('simple', 'simple'), ('complex', 'complex')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spanish_ws',
            name='item_cmplx29',
            field=models.CharField(max_length=20, null=True, choices=[('simple', 'simple'), ('complex', 'complex')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spanish_ws',
            name='item_prsube',
            field=models.CharField(max_length=20, null=True, choices=[('produces', 'produces')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spanish_ws',
            name='item_cmplx16',
            field=models.CharField(max_length=20, null=True, choices=[('simple', 'simple'), ('complex', 'complex')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spanish_ws',
            name='item_cmplx28',
            field=models.CharField(max_length=20, null=True, choices=[('simple', 'simple'), ('complex', 'complex')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spanish_ws',
            name='item_cmplx20',
            field=models.CharField(max_length=20, null=True, choices=[('simple', 'simple'), ('complex', 'complex')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spanish_ws',
            name='item_cmplx22',
            field=models.CharField(max_length=20, null=True, choices=[('simple', 'simple'), ('complex', 'complex')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spanish_ws',
            name='item_pasubi',
            field=models.CharField(max_length=20, null=True, choices=[('produces', 'produces')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spanish_ws',
            name='item_cmplx21',
            field=models.CharField(max_length=20, null=True, choices=[('simple', 'simple'), ('complex', 'complex')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spanish_ws',
            name='item_icome',
            field=models.CharField(max_length=20, null=True, choices=[('produces', 'produces')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='spanish_ws',
            name='item_cmplx19',
            field=models.CharField(max_length=20, null=True, choices=[('simple', 'simple'), ('complex', 'complex')]),
            preserve_default=True,
        ),
    ]
