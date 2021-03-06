# Generated by Django 2.2.10 on 2020-03-02 14:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200224_2253'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='dep_en',
        ),
        migrations.RemoveField(
            model_name='author',
            name='dep_ja',
        ),
        migrations.AddField(
            model_name='author',
            name='affiliation_en',
            field=models.TextField(blank=True, help_text='Affiliation (in English)(null=True, blank=True)', null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='affiliation_ja',
            field=models.TextField(blank=True, help_text='Affiliation (in Japanese)(null=True, blank=True)', null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='date_join',
            field=models.DateField(blank=True, help_text='The date which this author joinded to this department.(null=True, blank=True)', null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='date_leave',
            field=models.DateField(blank=True, help_text='The date which this author leave this department.(null=True, blank=True)', null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='mail',
            field=models.EmailField(blank=True, help_text='E-mail.(null=True, blank=True)', max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='name_en',
            field=models.CharField(help_text="The auhtor's full name in English. First name and family name should be split by space.See validation rules. (len=128).", max_length=128),
        ),
        migrations.AlterField(
            model_name='author',
            name='name_ja',
            field=models.CharField(blank=True, help_text="The author's full Name (Japanese). First name and family name should be split by space.See validation rules.  (len=128, null=True, blank=True)", max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='bibtex',
            name='abstruct',
            field=models.TextField(blank=True, help_text='Abstract of the paper.(blank=True)', null=True),
        ),
        migrations.AlterField(
            model_name='bibtex',
            name='authors',
            field=models.ManyToManyField(help_text="Authors of this publication. The order is stored based on ``AuthorOrder.order`` model.(model='Author', through='AuthorOrder').", through='core.AuthorOrder', to='core.Author'),
        ),
        migrations.AlterField(
            model_name='bibtex',
            name='bib_type',
            field=models.CharField(choices=[('AWARD', 'Award'), ('KEYNOTE', 'Keynote'), ('SAMEASBOOK', 'Same as the Book')], default='SAMEASBOOK', help_text='If this entry is related to an award or a presentation (not article),set this field. Otherwise, set SAMEASBOOK.(choose from ``BIBSTYLE_CHOICES``, see note for available choices.)', max_length=32),
        ),
        migrations.AlterField(
            model_name='bibtex',
            name='book',
            field=models.ForeignKey(help_text='Book object of this entry.(model=Book)', on_delete=django.db.models.deletion.PROTECT, to='core.Book'),
        ),
        migrations.AlterField(
            model_name='bibtex',
            name='book_title',
            field=models.CharField(blank=True, default='', help_text="The title of the book, if only part of it is being cited. This field include more detail information like year.For example, the title of book object is 'ICLR', set 'the 20th ICML'.(len=512, blank=True)", max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='bibtex',
            name='chapter',
            field=models.CharField(blank=True, help_text='The chapter number of a jounral. Before published, ignore this field.(len=128, blank=True)', max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='bibtex',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='bibtex',
            name='doi',
            field=models.CharField(blank=True, default='', help_text='The Digital Object Identifier.(len=128, optional)', max_length=128),
        ),
        migrations.AlterField(
            model_name='bibtex',
            name='edition',
            field=models.CharField(blank=True, help_text='The edition name. Before published, ignore this field. Check validation rule.(len=128, blank=True)', max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='bibtex',
            name='fund',
            field=models.CharField(blank=True, default='', help_text='Information about research fundings(e.g. JST CREST JPMJCR15E2).', max_length=512),
        ),
        migrations.AlterField(
            model_name='bibtex',
            name='is_published',
            field=models.BooleanField(blank=True, default=False, help_text='Set True when this paper has already published.(default: False)'),
        ),
        migrations.AlterField(
            model_name='bibtex',
            name='language',
            field=models.CharField(choices=[('EN', 'English'), ('JA', 'Japanese')], help_text='Default language setting for this publication. (choise=EN/JA', max_length=2),
        ),
        migrations.AlterField(
            model_name='bibtex',
            name='memo',
            field=models.CharField(blank=True, default='', help_text='Note or comment.(blank=True)', max_length=32),
        ),
        migrations.AlterField(
            model_name='bibtex',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='bibtex',
            name='number',
            field=models.CharField(blank=True, help_text="The '(issue) number' of a journal, magazine, or tech-report,if applicable. Note that this is not the 'article number' assigned by some journals.Before published, ignore this field.(len=128, blank=True)", max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='bibtex',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='bibtex',
            name='page',
            field=models.CharField(blank=True, help_text='page number. Before published, ignore this field. Check validation rule.(len=32, blank=True)', max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='bibtex',
            name='pub_date',
            field=models.DateField(blank=True, default='2000-01-01', help_text='The date (year, month, date) on which the book is published. If date-info is no needed, set 01 to the date field.(blank=True) (default: 2000-01-01)', null=True),
        ),
        migrations.AlterField(
            model_name='bibtex',
            name='tags',
            field=models.ManyToManyField(blank=True, help_text="Tags linked to this publication. (model='core.Tag', through='core.TagChain')", through='core.TagChain', to='core.Tag'),
        ),
        migrations.AlterField(
            model_name='bibtex',
            name='title_en',
            field=models.CharField(blank=True, default='', help_text='English title of this pubilication. Check validation rules.(len=512, blank=True)', max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='bibtex',
            name='title_ja',
            field=models.CharField(blank=True, default='', help_text='Japanese title of your pubilication. Check validation rules. (len=512, blank=True)', max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='bibtex',
            name='use_date_info',
            field=models.BooleanField(blank=True, default=False, help_text='If set True, the date will be displayed.(default: False)'),
        ),
        migrations.AlterField(
            model_name='bibtex',
            name='volume',
            field=models.CharField(blank=True, help_text='The volume of a journal or multi-volume book.Before published, ignore this field.(len=128, blank=True)', max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='abbr',
            field=models.CharField(blank=True, default='', help_text='The book title (Abbreviation).See validation. (len=256, null=True, blank=True)', max_length=256),
        ),
        migrations.AlterField(
            model_name='book',
            name='style',
            field=models.CharField(choices=[('Paper', (('JOURNAL', 'Journal'), ('INPROCEEDINGS', 'International Conference'), ('CONF_DOMESTIC', 'Domestic Conference'))), ('Article', (('BOOK', 'Book'), ('NEWS', 'News Paper'), ('MISC', 'Others'), ('ARTICLE', 'Article')))], help_text='Publication Type. See validation/type for the avaiable choises.(len=32, choice=``core.Book.STYLE_CHOICES``)', max_length=32),
        ),
    ]
