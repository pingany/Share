import sublime, sublime_plugin  

def removeNonAscii(s): return "".join(i for i in s if ord(i)<128)

class GitBlameCommand(sublime_plugin.TextCommand):  
    def run(self, edit, seeCommit=False):  
        import subprocess, os, sys, shlex, tempfile, re
        window = self.view.window()
        filename = self.view.file_name();
        dirname = os.path.dirname(filename);
        # print filename, dirname
        os.chdir(dirname)
        lines = subprocess.Popen(["git", "blame", os.path.basename(self.view.file_name())], stdout=subprocess.PIPE).communicate()[0]
        lines = lines.replace('\r', '').split('\n')
        current_lineno, current_columnno = self.view.rowcol(self.view.sel()[0].begin())
        # print current_lineno
        if current_lineno < len(lines):
            print lines[current_lineno]
            if seeCommit:
                line = lines[current_lineno]
                commit = re.split(r'\s', line, 1)[0]
                commit_content = subprocess.Popen(shlex.split("git log -p -n 1 %s" % commit), stdout=subprocess.PIPE).communicate()[0]
                commit_content = removeNonAscii(commit_content)
                # newfile = tempfile.NamedTemporaryFile(suffix=".diff")
                # print [line, commit, commit_content]
                # newfile = open("temp.diff", "w")
                # newfile.write(commit_content)
                # newfile.close()
                # newview = window.open_file(newfile.name)
                # newview.set_read_only(True)
                newview = window.new_file()
                newview.set_syntax_file('Packages/Diff/Diff.tmLanguage')
                newedit = newview.begin_edit()
                newview.insert(newedit, 0, commit_content)
                newview.end_edit(newedit)
        else:   
            print "not found lines"
        window.run_command("show_panel", {"panel" :"console"})
