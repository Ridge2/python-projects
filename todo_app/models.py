from django.db import models
from django.utils import timezone
from django.urls import reverse


# Create your models here

# return time 7 days time default
def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7)

# todo list model for database


class ToDoList(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def get_absolute_url(self):
        return reverse("list", args=[self.id])

    def __str__(self):
        return self.title

# todo item model for data storage


class ToDoItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    # default time from the model above
    due_date = models.DateTimeField(default=one_week_hence)
    # ToDoList becomes foreign key
    todo_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)  # *#

    def get_absolute_url(self):
        return reverse(
            "item-update", args=[str(self.todo_list.id), str(self.id)]
        )

    def __str__(self):
        return f"{self.title}: due {self.due_date}"
    # order by due date

    class Meta:
        ordering = ["due_date"]
