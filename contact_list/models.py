from django.db import models

# Create your models here.
class Contact(models.Model):
	name = models.CharField(blank=False, max_length=50)
	phone_number = models.CharField(blank=False, max_length=50)
	email = models.EmailField(blank=False)


	def __unicode__(self):
		return '%s'  % (self.name)

	class Meta:
		ordering =['name']
