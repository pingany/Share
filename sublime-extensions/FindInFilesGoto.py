# Usage:
# Add following line in "Preferences/Settings-User":
# { "keys": ["alt+enter"], "command": "find_in_files_goto"},

import sublime
import sublime_plugin
import re
import os
class FindInFilesGotoCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        window = view.window()

        targetGroup = self.getTargetGroup(window)
        activeGroup = window.active_group()
        print window.num_groups(), activeGroup, targetGroup
        
        if view.name() == "Find Results":
            newView = None
            line_no = self.get_line_no()
            file_name = self.get_file()
            if line_no is not None and file_name is not None:
                file_loc = "%s:%s" % (file_name, line_no)
                newView = view.window().open_file(file_loc, sublime.ENCODED_POSITION)
            elif file_name is not None:
                newView = view.window().open_file(file_name)

            if newView:
                if targetGroup != activeGroup :
                    window.set_view_index(newView, targetGroup, 0)
                window.focus_view(newView)

    def getTargetGroup(self, window):
        numGroups = window.num_groups()
        return (window.active_group() + 1) % numGroups

    def get_line_no(self):
        view = self.view
        if len(view.sel()) == 1:
            line_text = view.substr(view.line(view.sel()[0]))
            match = re.match(r"\s*(\d+).+", line_text)
            if match:
                return match.group(1)
        return None

    def get_file(self):
        view = self.view
        if len(view.sel()) == 1:
            line = view.line(view.sel()[0])
            while line.begin() > 0:
                line_text = view.substr(line)
                match = re.match(r"(.+):$", line_text)
                if match:
                    if os.path.exists(match.group(1)):
                        return match.group(1)
                line = view.line(line.begin() - 1)
        return None