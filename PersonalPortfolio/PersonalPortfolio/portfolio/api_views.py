from rest_framework import generics
from portfolio.models import Project, Skill, Experience, Education, Contact, About
from portfolio.serializers import ProjectSerializer, SkillSerializer, ExperienceSerializer, EducationSerializer, ContactSerializer, AboutSerializer


class ProjectList(generics.ListCreateAPIView):
    """
    A class used to represent a ProjectList

    Attributes
    ----------
    queryset : Project
        the queryset of the view
    serializer_class : ProjectSerializer
        the serializer class of the view
    """

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    A class used to represent a ProjectDetail

    Attributes
    ----------
    queryset : Project
        the queryset of the view
    serializer_class : ProjectSerializer
        the serializer class of the view
    """

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class SkillList(generics.ListCreateAPIView):
    """
    A class used to represent a SkillList

    Attributes
    ----------
    queryset : Skill
        the queryset of the view
    serializer_class : SkillSerializer
        the serializer class of the view
    """

    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class SkillDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    A class used to represent a SkillDetail

    Attributes
    ----------
    queryset : Skill
        the queryset of the view
    serializer_class : SkillSerializer
        the serializer class of the view
    """

    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class ExperienceList(generics.ListCreateAPIView):
    """
    A class used to represent an ExperienceList

    Attributes
    ----------
    queryset : Experience
        the queryset of the view
    serializer_class : ExperienceSerializer
        the serializer class of the view
    """

    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer


class ExperienceDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    A class used to represent an ExperienceDetail

    Attributes
    ----------
    queryset : Experience
        the queryset of the view
    serializer_class : ExperienceSerializer
        the serializer class of the view
    """

    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer


class EducationList(generics.ListCreateAPIView):
    """
    A class used to represent an EducationList

    Attributes
    ----------
    queryset : Education
        the queryset of the view
    serializer_class : EducationSerializer
        the serializer class of the view
    """

    queryset = Education.objects.all()
    serializer_class = EducationSerializer


class EducationDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    A class used to represent an EducationDetail

    Attributes
    ----------
    queryset : Education
        the queryset of the view
    serializer_class : EducationSerializer
        the serializer class of the view
    """

    queryset = Education.objects.all()
    serializer_class = EducationSerializer


class ContactList(generics.ListCreateAPIView):
    """
    A class used to represent a ContactList

    Attributes
    ----------
    queryset : Contact
        the queryset of the view
    serializer_class : ContactSerializer
        the serializer class of the view
    """

    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    A class used to represent a ContactDetail

    Attributes
    ----------
    queryset : Contact
        the queryset of the view
    serializer_class : ContactSerializer
        the serializer class of the view
    """

    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class AboutList(generics.ListCreateAPIView):
    """
    A class used to represent an AboutList

    Attributes
    ----------
    queryset : About
        the queryset of the view
    serializer_class : AboutSerializer
        the serializer class of the view
    """

    queryset = About.objects.all()
    serializer_class = AboutSerializer


class AboutDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    A class used to represent an AboutDetail

    Attributes
    ----------
    queryset : About
        the queryset of the view
    serializer_class : AboutSerializer
        the serializer class of the view
    """

    queryset = About.objects.all()
    serializer_class = AboutSerializer
