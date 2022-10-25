from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class AccountManager(BaseUserManager):
    # Create a New User;
    def create_user(self, email, username, password=None):
        # Base Checkpoint;
        if not(email):
            raise ValueError("Exception Traced: Required field missing (email)")
        if not(username):
            raise ValueError("Exception Traced: Required field missing (username)")

        email = self.normalize_email(email)
        
        user = self.model(email=email, username=username)
        user.set_password(password)
        user.save()
        return user

    # Create new Superuser;
    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username
        )
        
        is_admin = True
        is_active = True
        is_staff = True
        is_superuser = True
        user.save(using=self._db)
        
        return user


# Return the file image path;
def getProfileImagePath(self, filename):
    return f"media/profile_images/uid_{self.pk}/"

# Return the default image path;
def getDefaultProfileImage():
    return "media/avatar/avatar.png"


# Create your models here.
class Account(AbstractBaseUser):
    
    # ORM Attributes;
    email = models.EmailField(unique=True, max_length=128, verbose_name="email")
    username = models.CharField(unique=True, max_length=64, verbose_name="username")
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name="Date Joined")
    last_login = models.DateTimeField(auto_now_add=True, verbose_name="Last Login")
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    profile_image = models.ImageField(max_length=256, upload_to=getProfileImagePath, null=True, blank=True, default=getDefaultProfileImage)    
    hide_email = models.BooleanField(default=True)
    
    object = AccountManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    # Account class verbosity;
    def __str__():
        return f"Account (self.username)"
    
    # Return the filename of the profile image;
    def getProfileImageFilename(self):
        image = str(self.profile_image)
        return image[image.index(f"media/profile_images/uid_{self.pk}/"):]
    
    # ???
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    # ???
    def has_module_perms(self, app_label):
        return True
