from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


#   Custom Manager
# class TaggedItemManager(models.Manager):
#     def get_tags_for(self, obj_type, obj_id):
#         content_type = ContentType.objects.get_for_model(obj_type)
#         return TaggedItem.objects \
#             .select_related('tag') \
#             .filter(content_type=content_type, object_id=obj_id)


# class Tag(models.Model):
#     label = models.CharField(max_length=255)

#     def __str__(self):
#         return self.label


# class TaggedItem(models.Model):
#     #   Custom Manager
#     objects = TaggedItemManager()
#     tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
#     content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
#     object_id = models.PositiveIntegerField()
#     content_object = GenericForeignKey()

class Tag(models.Model):
    label = models.CharField(max_length=255)


class TaggedItem(models.Model):
    # what tag applied to what object
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    # Type (product , video , artical)
    # ID
    # to defind generic relationship y need to defind 3 fiels  1- contect_type 2-id 3-contect_object

    # -> ContentType :model that represent type of object in our application => allow Generic Relationship
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    product_id = models.PositiveIntegerField()
    # actual_object -> read the actual object that partuclar tag is apply too
    content_object = GenericForeignKey()
