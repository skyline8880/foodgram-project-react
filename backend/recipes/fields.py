import base64
import uuid

from django.core.files.base import ContentFile
from django.template.defaultfilters import slugify as django_slugify
from rest_framework import serializers
from unidecode import unidecode


class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            format, imgstr = data.split(';base64,')
            ext = format.split('/')[-1]
            id = uuid.uuid4()
            data = ContentFile(
                base64.b64decode(imgstr), name=id.urn[9:] + '.' + ext
            )
        return super().to_internal_value(data)


def unique_slugify(value, model):
    index = 0
    base_slug = django_slugify(unidecode(value))
    while True:
        unique_slug = '-'.join([base_slug, str(index)])
        if not model.objects.filter(slug=unique_slug).exists():
            return unique_slug
        index += 1
