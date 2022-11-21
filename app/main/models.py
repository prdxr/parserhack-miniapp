from django.db import models


# Create your models here.


class EventTypeClissifier(models.Model):
    """
    классификатор типов события
    """
    type_code = models.SmallIntegerField(primary_key=True)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description


class Tag(models.Model):
    """
    классификатор тегов
    """
    tag_code = models.SmallIntegerField(primary_key=True)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description


class HistoryUserRequest(models.Model):
    """
    модель для записей о времяни обращения конкретного пользователя к серверу
    """

    user_id = models.IntegerField(primary_key=True)
    time_of_last_request = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user_id


class Event(models.Model):
    """
    модель всех событий
    """
    title = models.CharField(max_length=255)
    description = models.TextField()

    address = models.CharField(max_length=255, blank=True, null=True)

    start_date = models.DateTimeField(blank=True, null=True)
    registration_deadline = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True,  null=True)

    url = models.URLField(max_length=255)
    img = models.URLField(max_length=255, null=True)

    type_of_event = models.ForeignKey(EventTypeClissifier, on_delete=models.DO_NOTHING)
    is_free = models.BooleanField(blank=True, null=True)

    tags = models.ManyToManyField(Tag, blank=True)

    date_of_parsing = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Event):
            return self.title == __o.title
        return False

