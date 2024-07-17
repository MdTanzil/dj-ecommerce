from django.apps import AppConfig
from oscar.core.application import OscarDashboardConfig


class HomeConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "home"


class HomeAppDashboardConfig(OscarDashboardConfig):
    name = "home"


default_app_config = "home.apps.HomeAppDashboardConfig"
