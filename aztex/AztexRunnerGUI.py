import wx

class AztexRunnerGUI(wx.Frame):

	def __init__(self, parent, title):
		super(AztexRunnerGUI, self).__init__(parent, title=title, size=wx.GetDisplaySize())
			
		self.InitUI()
		self.Centre()
		self.Show()   	

	def InitUI(self):
		self.panel = wx.Panel(self, -1)
		textWidth = self.size[0] / 2 - 6
		textHeight = self.size[1] - 6
		self.textCtrl = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE, pos=(3, 3), size=(textWidth, textHeight))

if __name__ == "__main__":

	app = wx.App()

	frame = AztexRunnerGUI(None, "Hello World")
	frame.Show()

	app.MainLoop()
