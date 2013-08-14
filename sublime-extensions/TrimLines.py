import sublime, sublime_plugin, re 
  
class TrimLinesCommand(sublime_plugin.TextCommand):  
    def run(self, edit):  
    	view = self.view
    	sels = view.sel()
    	#print sels
        if sels:
        	for sel in sels:
	        	originText = view.substr(sel)
	        	targetText = re.sub(r'([\t ]*)([\r\n])', r'\2', originText)
	        	#print [sel, originText, targetText]
	        	view.replace(edit, sel, targetText)
