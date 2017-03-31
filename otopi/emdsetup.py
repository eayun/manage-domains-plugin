"""engine manage domains setup."""

import os

from otopi import plugin, util

from ovirt_engine_setup import constants as osetupcons
from ovirt_engine_setup.engine import constants as oenginecons


@util.export
class Plugin(plugin.PluginBase):
    """engine manage domains setup."""

    @plugin.event(
        stage=plugin.Stages.STAGE_CLOSEUP,
        after=(
            osetupcons.Stages.DIALOG_TITLES_E_SUMMARY,
        ),
        condition=lambda self: (
            self.environment[oenginecons.EngineDBEnv.NEW_DATABASE]
        ),
    )
    def enable_engine_manage_domains_plugin(self):
        os.system("engine-manage-domains-setup")
        self.dialog.note(text="engine manage domains enabled.")

    @plugin.event(
        stage=plugin.Stages.STAGE_CLOSEUP,
        after=(
            osetupcons.Stages.DIALOG_TITLES_E_SUMMARY,
        ),
        condition=lambda self: (
            not self.environment[oenginecons.EngineDBEnv.NEW_DATABASE]
        ),
    )
    def restart_engine_manage_domains_plugin(self):
        os.system("service engine-manage-domains restart")
