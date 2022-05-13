import gdb
import os
import json

directory, file = os.path.split(__file__)
directory = os.path.expanduser(directory)
directory = os.path.abspath(directory)

with open(directory + '/plugins.json', 'r') as f:
    PLUGINS_MAPPING = json.load(f)

class GDBSwitch(gdb.Command):
    """
    A switch for switching gdb plugin
    """
    def __init__(self):
        super().__init__('gdbswitch', gdb.COMMAND_NONE)
    def invoke(self, arg, from_tty):
        arg = arg.strip()
        if '-e' in arg:
            # Load via environment variable
            env_variable = arg.split('-e')[-1].strip()
            plugin = os.environ.get(env_variable)
            plugin = plugin or PLUGINS_MAPPING['default']
            if plugin is None:
                print('You need to set the plugin name in the env variable or pass it by argument')
                return
        else:
            plugin = arg
        if plugin not in PLUGINS_MAPPING:
            print('Unknown plugin:', plugin)
            return
            
        pwd = os.getcwd()
        plugin_path = os.path.expanduser(PLUGINS_MAPPING[plugin])
        assert os.path.isfile(plugin_path)
        os.chdir(os.path.dirname(plugin_path))
        gdb.execute(f"source {plugin_path}")
        os.chdir(pwd)

GDBSwitch()
