"""engine manage domains setup."""

import os

from otopi import plugin, util

from ovirt_engine_setup import constants as osetupcons


@util.export
class Plugin(plugin.PluginBase):
    """engine manage domains setup."""

    @plugin.event(
        stage=plugin.Stages.STAGE_CLOSEUP,
        after=(
            osetupcons.Stages.DIALOG_TITLES_E_SUMMARY,
        ),
    )
    def enable_engine_manage_domains_plugin(self):
        os.system("engine-manage-domains-setup")
        self.dialog.note(text="engine manage domains enabled.")
