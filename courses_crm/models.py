from django.db import models

class Course(models.Model):
    image = models.ImageField(upload_to='course_images/', blank=True, null=True)
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    what_you_learn = models.TextField(blank=False, null=False)
    courses_included = models.TextField(blank=False, null=False)
    course_contents = models.TextField(blank=False, null=False)
    detailed_description = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.title

class TitleHeading(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='title_headings')
    heading = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return self.heading

class TitleHeadingDetail(models.Model):
    title_heading = models.ForeignKey(TitleHeading, on_delete=models.CASCADE, related_name='details')
    detail = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.detail[:50]  # Return a snippet of the detail text
