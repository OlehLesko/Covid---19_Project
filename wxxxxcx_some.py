import wx


class MyFrame2(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title='covid', pos=wx.DefaultPosition,
                          size=wx.Size(1366, 700), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        bSizer11 = wx.BoxSizer(wx.HORIZONTAL)
        self.img1 = wx.Image("image of main window.png", wx.BITMAP_TYPE_ANY)

        self.m_bitmap3 = wx.StaticBitmap(self, wx.ID_ANY, wx.BitmapFromImage(self.img1), wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        bSizer11.Add(self.m_bitmap3, 1, wx.EXPAND, 0)

        self.Bind(wx.EVT_SIZE, self.onResize)
        self.SetSizer(bSizer11)
        self.Layout()
        # self.Centre(wx.BOTH)

        self.button1 = wx.Button(
            self.m_bitmap3, label='Button1', size=(100, 100),
            pos=(100, 100))

        self.button1.Bind(wx.EVT_BUTTON, self.rdt)

    def rdt(self, event):
        print('Hello')

    def onResize(self, event):
        self.Layout()
        frame_size = self.GetSize()

        frame_h = (frame_size[0] - 10)
        frame_w = (frame_size[1] - 10)
        img1 = self.img1.Scale(frame_h, frame_w)

        self.m_bitmap3.SetBitmap(wx.BitmapFromImage(img1))

        self.Refresh()
        self.Layout()


app = wx.App(0)
MyFrame2(None).Show()
app.MainLoop()
