from configuration.models import Configuration
import random


def global_context(request):
    return {"configuration": Configuration.object()}