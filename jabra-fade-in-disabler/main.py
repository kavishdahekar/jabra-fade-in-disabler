import rumps
from sounds import AudioUtils

rumps.debug_mode(True)

class JabraDevolve(rumps.App):
    def __init__(self, name, title=None, icon=None):
        super(JabraDevolve, self).__init__(name=name,title=title,icon=icon)
        self.audio_utils = AudioUtils()

        # create menu status items
        self.menu_device_status = rumps.MenuItem("")
        self.menu_audio_stream_status = rumps.MenuItem("", callback=self.audio_stream_status_click)
        # self.menu_audio_stream_status.callback = self.audio_stream_status_click
        
        # update status menu items
        self.update_device_status()
        self.update_audio_stream_status()
        
        # add status items to menu
        self.menu.add(self.menu_device_status)
        self.menu.add(self.menu_audio_stream_status)

    def update_device_status(self):
        self.menu_device_status.title = "Jabra Detected 🟢" if self.audio_utils.jabraConnected else "Jabra Not Found 🔴"

    def update_audio_stream_status(self):
        self.menu_audio_stream_status.title = "Fade-In Disabled 🟢" if self.audio_utils.audioStreamEnabled else "Fade-In Enabled 🔴"

    def audio_stream_status_click(self, _):
        self.audio_utils.play_audio() if not self.audio_utils.audioStreamEnabled else self.audio_utils.stop_audio()
        self.update_audio_stream_status()

    # @rumps.clicked('Icon', 'On')
    # def a(self, _):
    #     self.icon = 'assets/ClippingSound.icns'

    # @rumps.clicked('Icon', 'Off')
    # def b(self, _):
    #     self.icon = 'assets/ClippingSound.icns'

    # @rumps.clicked("Silly button")
    # def onoff(self, sender):
    #     sender.state = not sender.state

    # @rumps.clicked("Say hi")
    # def sayhi(self, _):
    #     rumps.notification("Awesome title", "amazing subtitle", "hi!!1")

    @rumps.clicked("Refresh Devices")
    def refresh_devices(self, _):
        self.update_device_status()

if __name__ == "__main__":
    JabraDevolve(
        name="Jabra Devolve",
        # title="Jabra fade-in disable",
        icon="assets/ClippingSound.icns"
    ).run()