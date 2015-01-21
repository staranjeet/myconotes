from django.db import models

# class NewUrl(models.Model):

# 	def __str__(self):
# 		return self.url

# 	url =  models.CharField(max_length=10)
# 	gen_date = models.DateTimeField('date generated')

class Notes(models.Model):

	def __str__(self):
		return self.note

	url =  models.CharField(max_length=10)
	title = models.CharField(max_length=100)
	noteid = models.CharField(max_length=15)
	note = models.CharField(max_length=1000)
	noteGenDate=models.DateTimeField('note date generated')


