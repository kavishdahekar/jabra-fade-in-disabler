import logging
from ssl import AlertDescription
from typing_extensions import Self
import rumps
from sounds import AudioUtils
from utils import init_logger

init_logger()

class JabraDevolve(rumps.App):
    def __init__(self, name, title=None, icon=None):
        super(JabraDevolve, self).__init__(name=name,title=title,icon=icon,quit_button=None)
        self.audio_utils = AudioUtils()

        # create menu status items
        self.menu_device_status = rumps.MenuItem("")
        self.menu_audio_stream_status = rumps.MenuItem("", callback=self.audio_stream_status_click)

        # add status items to menu
        self.menu.add(self.menu_device_status)
        self.menu.add(self.menu_audio_stream_status)

        # update status menu
        self.update_device_status()
        # play audio
        self.audio_utils.play_audio()
        # update status menu
        self.update_audio_stream_status()

        logging.info("rumps app initialized")

    def update_device_status(self):
        self.menu_device_status.title = "Jabra Detected 🟢" if self.audio_utils.jabraConnected else "Jabra Not Found 🔴"

    def update_audio_stream_status(self):
        self.menu_audio_stream_status.title = "Fade-In Disabled 🟢" if self.audio_utils.audioStreamEnabled else "Fade-In Enabled 🔴"
        self.title = "🔈" if self.audio_utils.audioStreamEnabled else "🔇"

    def audio_stream_status_click(self, _):
        self.audio_utils.play_audio() if not self.audio_utils.audioStreamEnabled else self.audio_utils.stop_audio()
        self.update_audio_stream_status()

    @rumps.clicked("Refresh Devices")
    def refresh_devices(self, _):
        self.update_device_status()

    # @rumps.clicked("About")
    # def about(self, _):
    #     # rumps alerts do not seem to work on m1
    #     # rumps.alert(message='something')
    #     pass

    @rumps.clicked('Quit')
    def clean_up_before_quit(self, _):
        logging.info("clean up and quit")
        del self.audio_utils
        rumps.quit_application()

if __name__ == "__main__":
    JabraDevolve(
        name="Jabra Devolve",
        title="🔈"
    ).run()
