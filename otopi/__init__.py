"""engine manage domains plugin."""


from otopi import util


from . import emdsetup


@util.export
def createPlugins(context):
    emdsetup.Plugin(context=context)


# vim: expandtab tabstop=4 shiftwidth=4
