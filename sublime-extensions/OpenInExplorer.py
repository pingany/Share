import sublime, sublime_plugin

class OpenInExplorerCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        import subprocess, os
        subprocess.Popen(["nautilus", os.path.dirname(self.view.file_name())])