"""
	Displays the analogous .pdf document.

	code adapted from examples at:
		http://wiki.wxpython.org/Getting%20Started
		http://wiki.wxpython.org/WxHowtoSmallEditor?highlight=%28onsave%29
	uses wxPython library
"""

import wx, wx.lib.newevent, os
from main import main
from AztexCompiler import AztexCompiler

SaveEvent, EVT_SAVE = wx.lib.newevent.NewEvent()

class TextEditor(wx.Frame):
	""" Class for aztex text editor window """
	def __init__(self, parent, title):
		# Directory and file name of the document that is being edited
		self.dirname=''
		self.filename=''

		# Boolean value representing if the document has ever been saved before or not
		self.saved = False

		wx.Frame.__init__(self, parent, title=title, size=(700,750))
		self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
		self.CreateStatusBar() #status bar at bottom of window

		# Setting up menu
		filemenu = wx.Menu()
		menuOpen = filemenu.Append(wx.ID_OPEN, "&Open", " Open a file to edit")
		menuSave = filemenu.Append(wx.ID_SAVE, "&Save", "Save the document")
		menuSaveAs = filemenu.Append(wx.ID_SAVEAS, "&Save As...", "Save the document under a new name")
		menuAbout = filemenu.Append(wx.ID_ABOUT, "&About", "Informaiton about this program")
		menuExit = filemenu.Append(wx.ID_EXIT, "&Exit", "Terminate the program")

		# Making menubar
		menuBar = wx.MenuBar()
		menuBar.Append(filemenu, "&File")
		self.SetMenuBar(menuBar)

		# Events
		self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)
		self.Bind(wx.EVT_MENU, self.OnSave, menuSave)
		self.Bind(wx.EVT_MENU, self.OnSaveAs, menuSaveAs)
		self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
		self.Bind(wx.EVT_MENU, self.OnExit, menuExit)

		# self.sizer2 = wx.BoxSizer(wx.HORIZONTAL)
		# self.buttons = []
		# for i in range(0,6):
		# 	self.buttons.append(wx.Button(self, -1, "Button &"+str(i)))
		# 	self.sizer2.Add(self.buttons[i], 1, wx.EXPAND)

		self.sizer = wx.BoxSizer(wx.VERTICAL)
		self.sizer.Add(self.control, 1, wx.EXPAND)
		# self.sizer.Add(self.sizer2, 0, wx.EXPAND)

		self.SetSizer(self.sizer)
		self.SetAutoLayout(1)
		# self.sizer.Fit(self)
		self.Show()

	def get_text(self):
		text = ''
		for line in range(self.GetNumberOfLines):
			text += self.GetLineText(line) + '\n'
		return text

	def OnAbout(self, event):
		""" A message dialog box with an OK button """
		dlg = wx.MessageDialog(self, "aztex editor\naztex is a program that converts Markdown-like text into\nthe analogous LaTeX code to help in writing a pdf document", "About Sample Editor", wx.OK)
		dlg.ShowModal()
		dlg.Destroy()

	def OnSave(self, event):
		""" Save a file """
		if self.filename == '':
			self.OnSaveAs(event)
		else:
			with open(os.path.join(self.dirname, self.filename), 'w') as f:
				f.write(self.control.GetValue())
		return EVT_SAVE

	def OnSaveAs(self, event):
		dlg = wx.FileDialog(self, "", self.dirname, "", "*.*", wx.SAVE)
		if dlg.ShowModal() == wx.ID_OK:
			self.filename = dlg.GetFilename()
			self.dirname = dlg.GetDirectory()
			self.OnSave(event)
			self.SetTitle(self.filename)
			self.saved = True
		dlg.Destroy()

	def OnExit(self, event):
		""" Close the frame when exiting """
		self.Close(True)

	def OnOpen(self, event):
		""" Open a file """
		# self.dirname = ''
		dlg = wx.FileDialog(self, "", self.dirname, "", "*.*", wx.OPEN)
		if dlg.ShowModal() == wx.ID_OK:
			self.filename = dlg.GetFilename()
			self.dirname = dlg.GetDirectory()
			f = open(os.path.join(self.dirname, self.filename), 'r')
			self.control.SetValue(f.read())
			f.close()
			self.SetTitle(self.filename)
			self.saved = True
		dlg.Destroy()

class LatexViewer(wx.Frame):
	def __init__(self, parent, title, editor):
		self.editor = editor
		wx.Frame.__init__(self, parent, title=title, size=(700,750))
		# self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
		# self.CreateStatusBar() #status bar at bottom of window
		self.panel = wx.Panel(self, -1)
		self.text = "LaTeX code will appear here once the aztex code has been saved"
		self.font = wx.Font(10, wx.NORMAL, wx.NORMAL, wx.NORMAL)
		self.words = wx.StaticText(self.panel, -1, self.text, (30, 15))
		self.words.SetFont(self.font)

		self.aztexCompiler = AztexCompiler()
		self.Bind(wx.EVT_TEXT, self.update, self.editor.control)

		self.sizer = wx.BoxSizer(wx.VERTICAL)
		self.sizer.Add(self.panel, 1, wx.EXPAND)
		self.SetSizer(self.sizer)
		self.SetAutoLayout(1)
		self.Center()
		self.Show()

	def get_Latex_code(self):
		return self.aztexCompiler.compile(self.editor.control.GetValue)

	def update(self, event):
		self.text = self.get_Latex_code
		self.font = wx.Font(10, wx.NORMAL, wx.NORMAL, wx.NORMAL)
		self.words = wx.StaticText(self.panel, -1, self.text, (30, 15))
		self.words.SetFont(self.font)





if __name__ == "__main__":
	app = wx.App(False)
	frame = TextEditor(None, 'Untitled aztex Document')
	frameLatex = LatexViewer(None, 'Untitled .tex Document', frame)
	app.MainLoop()