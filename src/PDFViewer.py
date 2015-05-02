"""
	Displays the analogous .pdf document.
"""

import wx, os

class MyFrame(wx.Frame):
	""" Making a window """
	def __init__(self, parent, title):
		self.dirname=''

		wx.Frame.__init__(self, parent, title=title, size=(700,750))
		self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
		self.CreateStatusBar()

		filemenu = wx.Menu()
		menuOpen = filemenu.Append(wx.ID_OPEN, "&Open", " Open a file to edit")
		menuAbout = filemenu.Append(wx.ID_ABOUT, "&About", " Informaiton about this program")
		# self.Bind(wx.EVT_MENU, self.OnAbout, menuItem)
		# filemenu.AppendSeparator()
		menuExit = filemenu.Append(wx.ID_EXIT, "&Exit", " Terminate the program")

		menuBar = wx.MenuBar()
		menuBar.Append(filemenu, "&File")
		self.SetMenuBar(menuBar)

		self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)
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

		# self.Show(True)

	def OnAbout(self, event):
		""" A message dialog box with an OK button """
		dlg = wx.MessageDialog(self, "A small text editor \n in wxPython", "About Sample Editor", wx.OK)
		dlg.ShowModal()
		dlg.Destroy()

	def OnExit(self, event):
		self.Close(True)

	def OnOpen(self, event):
		""" Open a file """
		# self.dirname = ''
		dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", wx.OPEN)
		if dlg.ShowModal() == wx.ID_OK:
			self.filename = dlg.GetFilename()
			self.dirname = dlg.GetDirectory()
			f = open(os.path.join(self.dirname, self.filename), 'r')
			self.control.SetValue(f.read())
			f.close()
		dlg.Destroy()

app = wx.App(False)
frame = MyFrame(None, 'Sample editor')
app.MainLoop()