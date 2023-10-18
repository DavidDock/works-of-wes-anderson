from films.models import Film

""" Learnt from
https://djangocentral.com/how-to-create-custom-context-processors-in-django/
This is to give each template all film objects
"""


def films(request):
    return {'films': Film.objects.all()}
