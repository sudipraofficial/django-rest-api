from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserManagerClass(BaseUserManager):
    """Class to manage user Class"""

    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError("User must have email address")
        
        email = self.normalize_email(email)
        print(email)
        user = self.model(email=email, name=name)
        print(user)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password=None):
        """"Create and save a new super user with given details"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)
        
        return user
         

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Class to create user for system"""
    email = models.EmailField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManagerClass()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retreive full name for the user"""
        return self.name
    
    def get_short_name(self):
        """Retreive short name for the user"""
        return self.name
    
    def __str__(self):
        """"Return string representation of the User model"""
        return self.email


