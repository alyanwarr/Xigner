from burp import IBurpExtender
from burp import IMessageEditorTabFactory
from burp import IMessageEditorTab
import re

class BurpExtender(IBurpExtender, IMessageEditorTabFactory):
    
    def	registerExtenderCallbacks(self, callbacks):
    	
    	#seting the extension name & registering the message editor 
    	
        self._callbacks = callbacks
        self._helpers = callbacks.getHelpers()
        callbacks.setExtensionName("Xigner")
	callbacks.registerMessageEditorTabFactory(self)
         
         #implementing the IMessageEditorTabFactory
         
    def createNewInstance(self, controller, editable): 
        return SignXMLInputTab(self, controller, editable)
        
class SignXMLInputTab(IMessageEditorTab):
    def __init__(self, extender, controller, editable):
    
        self._extender = extender
        self._editable = editable
        self._txtInput = extender._callbacks.createTextEditor()
        self._txtInput.setEditable(editable)

    def getTabCaption(self):
        return "Signed XML"
        
    def getUiComponent(self):
        return self._txtInput.getComponent()
        
    def isEnabled(self, content, isRequest):
        return isRequest
        
    def setMessage(self, content, isRequest):
    
    	# copy the HTTP request 
	tmp = content
	
        if content is None:
            self._txtInput.setEditable(False)
        
        else:
            # retrieve the <example> tag values from POST body            
            # Save in temp.txt
	    # Sign then update current display

            xml = re.search(r'<example>([\s\S]+?)</example>',content, re.IGNORECASE).group()
            
	    final_xml = xml.replace("\n","").replace("\r","")
	    
            with open("temp.txt","w") as f:
                f.write(final_xml)
                
            # very ugly, but Jython does not support libxml yet AFAIK
            res = os.popen("python sign.py").read()
            
            # prints the result to screen
	    self._updatedcontent = (self._extender._helpers.bytesToString(tmp)).replace(xml,res)
            self._txtInput.setText("******** Signed Successfully ********\n\n"+res)
            self._txtInput.setEditable(True)
        
        self._currentMessage = content
    
    def getMessage(self):
	return self._updatedcontent
    
    def isModified(self):
	# auto-update the current display
        return True
    
    def getSelectedData(self):
        return self._txtInput.getSelectedText()
