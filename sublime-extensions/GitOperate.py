# Usage:
# Add following line(s) in "Preferences/Settings-User":
# {"keys": ["alt+f6"], "command": "git_operate", "args" : {"action" : "add"}},
# {"keys": ["alt+f5"], "command": "git_operate", "args" : {"action" : "rm -f"}},

import sublime, sublime_plugin  

def removeNonAscii(s): return "".join(i for i in s if ord(i)<128)

class GitOperateCommand(sublime_plugin.TextCommand):  
    def run(self, edit, action):  
        import subprocess, os, sys, shlex, tempfile, re, commands
        window = self.view.window()
        filename = self.view.file_name();
        dirname = os.path.dirname(filename);
        # print filename, dirname
        os.chdir(dirname)
        print commands.getstatusoutput("git %s %s " %(action, os.path.basename(filename)));
        window.run_command("show_panel", {"panel" :"console"})