from libnetid.django.models import AbstractNetidUser


class User(AbstractNetidUser):
    def as_dict(self):
        return {
            'netid': self.netid,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
        }
