from django.db import models

class Page(models.Model):
  """
  Wiki page content
  """
  title = models.CharField(max_length="20", primary_key=True)
  content = models.TextField(blank=True)

#  def __str__(self):
#    return u"%s" % self.title
