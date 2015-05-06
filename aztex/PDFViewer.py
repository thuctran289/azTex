"""
	Displays the analogous LaTeX code.

	code adapted from examples at:
		http://wiki.wxpython.org/Getting%20Started
		http://wiki.wxpython.org/WxHowtoSmallEditor?highlight=%28onsave%29
	uses wxPython library
"""

import wx, wx.lib.newevent, os
from main import main
from AztexCompiler import AztexCompiler

class AztexGUI(wx.Frame):
	""" Class for editing aztex code and viewing analogous LaTeX code """
	def __init__(self, parent, title):
		wx.Frame.__init__(self, parent, title=title, size=(800, 750))
		self.panel = wx.Panel(self)
		self.aztexEditor = AztexEditor(self.panel)
		self.latexViewer = LatexViewer(self.panel)

		# initialize an AztexCompiler to compile the aztex
		# code from self.editor into analogous LaTeX code
		self.aztexCompiler = AztexCompiler()

		self.CreateStatusBar() #status bar at bottom of window

		# Setting up menu
		filemenu = wx.Menu()
		menuOpen = filemenu.Append(wx.ID_OPEN, "&Open", " Open a file to edit")
		menuSaveAztex = filemenu.Append(wx.ID_SAVE, "&Save aztex", "Save the aztex .txt document")
		menuSaveAsAztex = filemenu.Append(wx.ID_SAVEAS, "&Save As aztex...", "Save the aztex .txt document under a new name")
		menuSaveLatex = filemenu.Append(wx.ID_SAVE, "&Save LaTeX", "Save the .tex document")
		menuSaveAsLatex = filemenu.Append(wx.ID_SAVEAS, "&Save As LaTeX...", "Save the .tex document under a new name")
		menuAbout = filemenu.Append(wx.ID_ABOUT, "&About", "Informaiton about this program")
		menuExit = filemenu.Append(wx.ID_EXIT, "&Exit", "Terminate the program")

		# Making menubar
		menuBar = wx.MenuBar()
		menuBar.Append(filemenu, "&File")
		self.SetMenuBar(menuBar)

		# Events
		self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)
		self.Bind(wx.EVT_MENU, self.OnSaveAztex, menuSaveAztex)
		self.Bind(wx.EVT_MENU, self.OnSaveAsAztex, menuSaveAsAztex)
		self.Bind(wx.EVT_MENU, self.OnSaveLatex, menuSaveLatex)
		self.Bind(wx.EVT_MENU, self.OnSaveAsLatex, menuSaveAsLatex)
		self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
		self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
		self.Bind(wx.EVT_TEXT, self.update_latex_viewer, self.aztexEditor)

		# Add sizer
		self.sizer = wx.BoxSizer(wx.HORIZONTAL)
		self.sizer.Add(self.aztexEditor, 1, wx.EXPAND)
		self.sizer.Add(self.latexViewer, 1, wx.EXPAND)

		# Show the frame
		self.SetSizer(self.sizer)
		self.Centre()
		self.SetAutoLayout(1)
		self.Show()

	def OnAbout(self, event):
		""" A message dialog box with an OK button """
		dlg = wx.MessageDialog(self, "aztex editor\naztex is a program that converts Markdown-like text into\nthe analogous LaTeX code to help in writing a pdf document", "About Sample Editor", wx.OK)
		dlg.ShowModal()
		dlg.Destroy()

	def OnSaveAztex(self, event):
		""" Save aztex file """
		if self.aztexEditor.filename == '': # if document is currently unsaved
			self.OnSaveAs(event)
		else: # if document has previously been saved
			with open(os.path.join(self.aztexEditor.dirname, self.aztexEditor.filename), 'w') as f:
				f.write(self.aztexEditor.GetValue())

	def OnSaveAsAztex(self, event):
		""" Save As the aztex file """
		dlg = wx.FileDialog(self, "", self.aztexEditor.dirname, "", "*.*", wx.SAVE)
		if dlg.ShowModal() == wx.ID_OK: # if user clicks OK (if user wants to save the document)
			self.aztexEditor.filename = dlg.GetFilename()
			self.aztexEditor.dirname = dlg.GetDirectory()
			self.OnSaveAztex(event)
			self.SetTitle(self.aztexEditor.filename)
		dlg.Destroy()

	def OnSaveLatex(self, event):
		""" Save LaTeX file """
		if self.latexViewer.filename == '': # if document is currently unsaved
			self.OnSaveAsLatex(event)
		else: # if document has previously been saved
			with open(os.path.join(self.latexViewer.dirname, self.latexViewer.filename), 'w') as f:
				f.write(self.latexViewer.GetValue())

	def OnSaveAsLatex(self, event):
		""" Save As LaTeX file """
		dlg = wx.FileDialog(self, "", self.latexViewer.dirname, "", "*.*", wx.SAVE)
		if dlg.ShowModal() == wx.ID_OK: # if user clicks OK (if user wants to save the document)
			self.latexViewer.filename = dlg.GetFilename()
			self.latexViewer.dirname = dlg.GetDirectory()
			self.OnSaveLatex(event)
		dlg.Destroy()

	def OnExit(self, event):
		""" Close the frame when exiting """
		self.Close(True)

	def OnOpen(self, event):
		""" Open a file to the AztexEditor """
		dlg = wx.FileDialog(self, "", self.aztexEditor.dirname, "", "*.*", wx.OPEN)
		if dlg.ShowModal() == wx.ID_OK: # if user clicks OK (if user wants to open a document)
			self.aztexEditor.filename = dlg.GetFilename()
			self.aztexEditor.dirname = dlg.GetDirectory()
			f = open(os.path.join(self.aztexEditor.dirname, self.aztexEditor.filename), 'r')
			self.aztexEditor.SetValue(f.read())
			f.close()
			self.SetTitle(self.aztexEditor.filename)
		dlg.Destroy()

	def update_latex_viewer(self, event):
		""" get the analogous LaTeX code from the aztex code  """
		# use try/except so that even if there is an error compiling, after
		# after removing the problematic aztex code, the user can continue to
		# write in the aztex compiler and have new, non-erronous code be
		# compiled into LaTeX code
		try:
			self.latexViewer.SetValue(self.aztexCompiler.compile(str(self.aztexEditor.GetValue()))) 	# way 1 of getting text
			# self.latexViewer.SetValue(self.aztexCompiler.compile(str(self.aztexEditor.get_text())))	# way 2 of getting text
			self.SetStatusText('')
		except: #TypeError, AttributeError
			self.SetStatusText("there's an error compiling :(")


class AztexEditor(wx.TextCtrl):
	""" Class for aztex text editor TextCtrl """
	def __init__(self, panel):
		wx.TextCtrl.__init__(self, panel, style=wx.TE_MULTILINE)
		# Directory and file name of the document that is being edited
		self.dirname=''
		self.filename=''

	def get_text(self):
		""" Returns the text in the AztexEditor """
		text = ''
		for line in range(self.GetNumberOfLines()):
			text += str(self.GetLineText(line)) + '\n'
		return str(text)

class LatexViewer(wx.TextCtrl):
	"""
		Class representing the TextCtrl that displays the LaTeX code analogous to
		the aztex code being entered in an AztexGUI's AztexEditor that contains 
		the LatexViewer
	"""
	def __init__(self, panel):
		wx.TextCtrl.__init__(self, panel, value="LaTeX code will appear here once the aztex code has been edited", style = wx.TE_MULTILINE)
		self.dirname = ''
		self.filename = ''

if __name__ == "__main__":
	app = wx.App(False)
	frame = AztexGUI(None, 'Untitled aztex Document')
	app.MainLoop()