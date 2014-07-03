# Usage:
# Add this file in sublime extension directory, for linux it is ~/.config/sublime-text-*/Packages/User
# Add following line in "Preferences/Settings-User":
# {"keys": ["alt+f11"], "command": "git_blame"},
# And then go to source code, put cursor on a line, press "alt+f11", you will see the whole commit which modify this line in the last time.

# Both support sublime-2 and sublime-3

import sublime, sublime_plugin

def removeNonAscii(s): return "".join(i for i in s if ord(i)<128)

class GitBlameCommand(sublime_plugin.TextCommand):
    def run(self, edit, seeCommit=True):
        import subprocess, os, sys, shlex, tempfile, re
        window = self.view.window()
        filename = self.view.file_name();
        dirname = os.path.dirname(filename);
        # print filename, dirname
        os.chdir(dirname)
        lines = subprocess.Popen(["git", "blame", os.path.basename(self.view.file_name())], stdout=subprocess.PIPE).communicate()[0]
        linesStr = lines.decode()
        # print(linesStr)
        lines = re.split(r'\r?\n', linesStr)
        #print(lines)
        current_lineno, current_columnno = self.view.rowcol(self.view.sel()[0].begin())
        # print(current_lineno)
        # print(current_columnno)
        if current_lineno < len(lines):
            print(lines[current_lineno])
            if seeCommit:
                line = lines[current_lineno]
                commit = re.split(r'\s', line, 1)[0]
                # print(commit)
                commit_content = subprocess.Popen(shlex.split("git log -p -n 1 %s" % str(commit)), stdout=subprocess.PIPE).communicate()[0]
                newfile = tempfile.NamedTemporaryFile(suffix=".diff", delete=False)
                newfile.write(commit_content)
                newfile.close()
                newview = window.open_file(newfile.name)
                newview.set_read_only(True)
                newview.set_syntax_file('Packages/Diff/Diff.tmLanguage')
        else:
            print("not found lines")
        window.run_command("show_panel", {"panel" :"console"})
