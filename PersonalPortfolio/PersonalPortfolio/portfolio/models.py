from django.db import models


class Project(models.Model):
    """
    A class used to represent a Project

    Attributes
    ----------
    title : str
        the title of the project
    description : str
        the description of the project
    url : str
        the url of the project

    Methods
    -------
    __str__()
        Returns the title of the project
    """

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250, blank=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title


class Skill(models.Model):
    """
    A class used to represent a Skill

    Attributes
    ----------
    title : str
        the title of the skill
    description : str
        the description of the skill

    Methods
    -------
    __str__()
        Returns the title of the skill
    """

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.title


class Experience(models.Model):
    """
    A class used to represent an Experience

    Attributes
    ----------
    title : str
        the title of the experience
    description : str
        the description of the experience
    start_date : date
        the start date of the experience

    Methods
    -------
    __str__()
        Returns the title of the experience
    """

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title


class Education(models.Model):
    """
    A class used to represent an Education

    Attributes
    ----------
    title : str
        the title of the education
    description : str
        the description of the education
    start_date : date
        the start date of the education
    end_date : date
        the end date of the education

    Methods
    -------
    __str__()
        Returns the title of the education
    """

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    """
    A class used to represent a Contact

    Attributes
    ----------
    email : str
        the email of the contact
    phone : str
        the phone of the contact
    address : str
        the address of the contact
    linkedin : str
        the linkedin of the contact
    github : str
        the github of the contact

    Methods
    -------
    __str__()
        Returns the email of the contact
    """

    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=250)
    linkedin = models.URLField()
    github = models.URLField()

    def __str__(self):
        return self.email


class About(models.Model):
    """
    A class used to represent an About

    Attributes
    ----------
    description : str
        the description of the about

    Methods
    -------
    __str__()
        Returns the description of the about
    """

    description = models.CharField(max_length=250)
    # image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.description
