import os
import logging
import wave
import sounddevice as sd
import numpy as np

from utils import get_bool_env_var, resource_path

class AudioUtils:

    def __init__(self):
        self.audio_sample = None
        self.sample_rate = None
        self.audio_stream_enabled = False
        self.audio_file_name = "assets/audio_sample.wav" if not get_bool_env_var('JABRA_DEVOLVE_DEBUG') else "assets/audio_sample_debug.wav"
        _ = self.jabraConnected
        self.read_audio_sample()

    def reIntializeSound(self):
        # workaround for stale read by query_devices
        # https://github.com/spatialaudio/python-sounddevice/issues/125#issuecomment-372281215
        sd._terminate()
        sd._initialize()
        # ensure audio is resumed when devices are refreshed
        if self.audio_stream_enabled:
            self.play_audio()
        logging.info("reinitialized")

    def read_audio_sample(self):
        # Read file to get buffer
        # Less CPU intensive than generating a sine wave
        ifile = wave.open(resource_path(self.audio_file_name))
        samples = ifile.getnframes()
        audio = ifile.readframes(samples)

        # Convert buffer to float32 using NumPy                                                                                 
        audio_as_np_int16 = np.frombuffer(audio, dtype=np.int16)
        audio_as_np_float32 = audio_as_np_int16.astype(np.float32)

        # Normalise float32 array so that values are between -1.0 and +1.0                                                      
        max_int16 = 2**15
        self.audio_sample = audio_as_np_float32 / max_int16
        logging.info("audio sample ready")

    @property
    def jabraConnected(self):
        self.reIntializeSound()
        devices = sd.query_devices()
        logging.info("devices : %s",devices)
        try:
            _ = next(item for item in devices if "Jabra" in item["name"] and item["max_output_channels"] > 0)
            return True
        except Exception:
            return False

    def play_audio(self):
        logging.info("playing audio")
        sd.play(self.audio_sample, loop=True)
        self.audio_stream_enabled = True
        logging.info("audio_stream_enabled : %s", self.audio_stream_enabled)

    def stop_audio(self):
        logging.info("stopping audio")
        sd.stop()
        self.audio_stream_enabled = False
        logging.info("audio_stream_enabled : %s", self.audio_stream_enabled)

    @property
    def audioStreamEnabled(self):
        return self.audio_stream_enabled
