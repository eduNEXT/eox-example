"""
App configuration for eox_example.
"""

from __future__ import unicode_literals

from django.apps import AppConfig


class EoxExampleConfig(AppConfig):
    """
    eduNEXT example plugin configuration.
    """

    name = "eox_example"
    verbose_name = "eduNEXT example plugin"

    plugin_app = {
        "url_config": {
            "lms.djangoapp": {
                "namespace": "eox_example",
                "regex": r"^eox_example/",
                "relative_path": "urls",
            },
            "cms.djangoapp": {
                "namespace": "eox_example",
                "regex": r"^eox_example/",
                "relative_path": "urls",
            },
        },
        "settings_config": {
            "lms.djangoapp": {
                "common": {"relative_path": "settings.common"},
                "test": {"relative_path": "settings.test"},
                "aws": {"relative_path": "settings.aws"},
                "production": {"relative_path": "settings.production"},
            },
            "cms.djangoapp": {
                "common": {"relative_path": "settings.common"},
                "test": {"relative_path": "settings.test"},
                "aws": {"relative_path": "settings.aws"},
                "production": {"relative_path": "settings.production"},
            },
        },
        "view_context_config": {
            "lms.djangoapp": {
                "course_dashboard": "eox_exampl.context.get_dashboard_context"
            }
        },
        "actions_config": {
            "lms.djangoapp": {"post_login": "eox_example.actions.post_login"}
        },
    }
