from django.db import models
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify
import datetime
from djangotoolbox.fields import ListField, EmbeddedModelField
import urllib
import BeautifulSoup


class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    title = models.CharField(max_length=255)    
    url = models.URLField(max_length=200)
    slug = models.SlugField()

    description = models.CharField(max_length=255)
    notes = ListField(EmbeddedModelField('Note'), editable=False)

    #def save(self):
        #soup = BeautifulSoup.BeautifulSoup(urllib.urlopen(self.url))
        #self.title = soup.title.string
        #super(Post, self).save()
        #date = datetime.date.today()
        #self.slug = '%i/%i/%i/%s' % (
        #    date.year, date.month, date.day, slugify(self.url)
        #)
        #super(Post, self).save()

    def get_absolute_url(self):
        return reverse('post', kwargs={"slug": self.slug})

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ["-created_at"]


class Note(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    body = models.TextField(verbose_name="Note")
    author = models.CharField(verbose_name="Name", max_length=255)