# Usage:
# Add following line in "Preferences/Settings-User":
# {"keys": ["f8"], "command": "open_in_explorer"},

import sublime, sublime_plugin

class OpenInExplorerCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        import subprocess, os
        subprocess.Popen(["nautilus", os.path.dirname(self.view.file_name())])