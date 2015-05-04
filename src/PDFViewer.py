"""
	Displays the analogous .pdf document.

	code adapted from examples at:
		http://wiki.wxpython.org/Getting%20Started
		http://wiki.wxpython.org/WxHowtoSmallEditor?highlight=%28onsave%29
	uses wxPython library
"""

import wx, os, 

class TextEditor(wx.Frame):
	""" Making a window """
	def __init__(self, parent, title):
		self.dirname=''
		self.filename=''

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

		self.sizer2 = wx.BoxSizer(wx.HORIZONTAL)
		self.buttons = []
		for i in range(0,6):
			self.buttons.append(wx.Button(self, -1, "Button &"+str(i)))
			self.sizer2.Add(self.buttons[i], 1, wx.EXPAND)

		self.sizer = wx.BoxSizer(wx.VERTICAL)
		self.sizer.Add(self.control, 1, wx.EXPAND)
		self.sizer.Add(self.sizer2, 0, wx.EXPAND)

		self.SetSizer(self.sizer)
		self.SetAutoLayout(1)
		self.sizer.Fit(self)
		self.Show()

	def OnAbout(self, event):
		""" A message dialog box with an OK button """
		dlg = wx.MessageDialog(self, "A small text editor \n in wxPython", "About Sample Editor", wx.OK)
		dlg.ShowModal()
		dlg.Destroy()

	def OnSave(self, event):
		""" Save a file """
		if self.filename == '':
			self.OnSaveAs(event)
		else:
			with open(os.path.join(self.dirname, self.filename), 'w') as f:
				f.write(self.control.GetValue())

	def OnSaveAs(self, event):
		dlg = wx.FileDialog(self, "", self.dirname, "", "*.*", wx.SAVE)
		if dlg.ShowModal() == wx.ID_OK:
			self.filename = dlg.GetFilename()
			self.dirname = dlg.GetDirectory()
			self.OnSave(event)
			self.SetTitle(self.filename)
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
		dlg.Destroy()

class LatexViewer(wx.Frame):
	def __init__(self, parent, title, editor):




if __name__ == "__main__":
	app = wx.App(False)
	frame = TextEditor(None, 'Untitled Document')
	app.MainLoop()