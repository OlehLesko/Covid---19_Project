import wx
from win32api import GetSystemMetrics
import wx.lib.stattext as ST


w = GetSystemMetrics(0)
h = GetSystemMetrics(1)
print("Width =", GetSystemMetrics(0))
print("Height =", GetSystemMetrics(1))
start_position_high_button = int(h / 2 - 86)


class Start(wx.Frame):
    def __init__(self, parent, title):
        super(Start, self).__init__(parent, title=title, pos=(0, 0), size=(w, h))
        self.m_bitmap3 = None
        self.img1 = None
        self.buttons = []
        self.button = None
        self.bitmap()

    def bitmap(self):

        box_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.img1 = wx.Image("Images/image of main window.png", wx.BITMAP_TYPE_ANY)
        self.m_bitmap3 = wx.StaticBitmap(self, id=wx.ID_ANY, bitmap=wx.Bitmap(self.img1), pos=wx.DefaultPosition,
                                         size=wx.DefaultSize, style=0, name=wx.StaticBitmapNameStr)
        # st1 = ST.GenStaticText(self.m_bitmap3, -1, "This is an example of static text", (20, 10))

        box_sizer.Add(self.m_bitmap3, 1, wx.EXPAND, 0)
        self.Bind(wx.EVT_SIZE, self.resize)
        self.SetSizer(box_sizer)

    def create_button(self, m_bimap3, id, label, size, pos):
        button = f'button_{id}'
        print(button)
        button = wx.Button(
            self.m_bitmap3, label=label, size=size, pos=pos)
        print(button)
        if id == 1:
            self.Bind(wx.EVT_BUTTON, self.europe, button)
        if id == 2:
            self.Bind(wx.EVT_BUTTON, self.ukraine, button)
        if id == 3:
            self.Bind(wx.EVT_BUTTON, self.asia, button)

    def europe(self, event):

        print('Hello1')

    def ukraine(self, event):
        print('Hello2')

    def asia(self, event):
        print('Hello3')

    def resize(self, event):
        self.Layout()
        frame_size = self.GetSize()
        print(f'frame_size={frame_size}')
        frame_h = (frame_size[0] - 10)
        frame_w = (frame_size[1] - 10)
        img1 = self.img1.Scale(frame_h, frame_w)
        print(frame_h)
        if frame_h < 824:
            self.destroy_bitmap()
            self.bitmap()
            self.create_button(self.m_bitmap3, 1, "Europe", (153, 86), (int(frame_h / 2 - 76), int(frame_h / 3)))
            self.create_button(self.m_bitmap3, 2, "Ukraine", (153, 86), (int(frame_h / 2 - 76), int(frame_h / 3 + 100)))
            self.create_button(self.m_bitmap3, 3, "Asia", (153, 86), (int(frame_h / 2 - 76), int(frame_h / 3 + 200)))

        else:
            self.destroy_bitmap()
            self.bitmap()
            self.create_button(self.m_bitmap3, 1, "Europe", (153, 86), (120, start_position_high_button))
            self.create_button(self.m_bitmap3, 2, "Ukraine", (153, 86), (320, start_position_high_button))
            self.create_button(self.m_bitmap3, 3, "Asia", (153, 86), (520, start_position_high_button))
        self.m_bitmap3.SetBitmap(wx.Bitmap(img1))

        self.Refresh()
        self.Layout()
    def destroy_bitmap(self):
        self.m_bitmap3.Destroy()

def main():
    app = wx.App()
    start = Start(None, "Start application")
    start.Show()
    app.MainLoop()


if __name__ == "__main__":
    main()
