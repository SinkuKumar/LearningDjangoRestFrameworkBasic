from .models import Project, Skill, Experience, Education, Contact, About
from rest_framework import serializers


class ProjectSerializer(serializers.ModelSerializer):
    """
    A class used to serialize a Project

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

    class Meta:
        """
        A class used to represent the metadata of the ProjectSerializer

        Attributes
        ----------
        model : Project
            the model to serialize
        fields : list
            the fields to serialize
        """

        model = Project
        fields = "__all__"


class SkillSerializer(serializers.ModelSerializer):
    """
    A class used to serialize a Skill

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

    class Meta:
        """
        A class used to represent the metadata of the SkillSerializer

        Attributes
        ----------
        model : Skill
            the model to serialize
        fields : list
            the fields to serialize
        """

        model = Skill
        fields = "__all__"


class ExperienceSerializer(serializers.ModelSerializer):
    """
    A class used to serialize an Experience

    Attributes
    ----------
    title : str
        the title of the experience
    description : str
        the description of the experience
    start_date : date
        the start date of the experience
    end_date : date
        the end date of the experience

    Methods
    -------
    __str__()
        Returns the title of the experience
    """

    class Meta:
        model = Experience
        fields = "__all__"


class EducationSerializer(serializers.ModelSerializer):
    """
    A class used to serialize an Education

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

    class Meta:
        """
        A class used to represent the metadata of the EducationSerializer

        Attributes
        ----------
        model : Education
            the model to serialize
        fields : list
            the fields to serialize
        """

        model = Education
        fields = "__all__"


class ContactSerializer(serializers.ModelSerializer):
    """
    A class used to serialize a Contact

    Attributes
    ----------
    name : str
        the name of the contact
    email : str
        the email of the contact
    subject : str
        the subject of the contact
    message : str
        the message of the contact

    Methods
    -------
    __str__()
        Returns the name of the contact
    """

    class Meta:
        """
        A class used to represent the metadata of the ContactSerializer

        Attributes
        ----------
        model : Contact
            the model to serialize
        fields : list
            the fields to serialize
        """

        model = Contact
        fields = "__all__"


class AboutSerializer(serializers.ModelSerializer):
    """
    A class used to serialize an About object

    Attributes
    ----------
    title : str
        the title of the about
    description : str
        the description of the about
    image : str
        the image of the about

    Methods
    -------
    __str__()
        Returns the title of the about
    """

    class Meta:
        """
        A class used to represent the metadata of the AboutSerializer

        Attributes
        ----------
        model : About
            the model to serialize
        fields : list
            the fields to serialize
        """

        model = About
        fields = "__all__"
