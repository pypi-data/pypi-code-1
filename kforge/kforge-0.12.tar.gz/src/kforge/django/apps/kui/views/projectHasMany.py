from dm.view.base import *
from kforge.django.apps.kui.views.project import ProjectInstanceView
import kforge.command
from kforge.exceptions import KforgeCommandError


class ProjectHasManyView(AbstractHasManyView, ProjectInstanceView):

    pass

