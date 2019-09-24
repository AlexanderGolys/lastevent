from django.contrib.auth.base_user import BaseUserManager



class FuneralUserManager(BaseUserManager):
    def create_user(self, username, **kwargs):
        user = self.model(username=username, **kwargs)
        user.save()
        return user

    def create_superuser(self, username, **kwargs):
        user = self.model(username=username, **kwargs)
        user.is_admin = True
        user.is_staff = True


