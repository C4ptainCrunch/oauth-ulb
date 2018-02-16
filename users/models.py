from django.db import models
import libnetid.django.models.AbstractNetidUser


class User(libnetid.django.models.AbstractNetidUser):
    full_xml = models.TextField()
