import wave
import sounddevice as sd
import numpy as np

class AudioUtils:

    def __init__(self):
        self.audio_sample = None
        self.sample_rate = None
        self.audio_stream_enabled = False
        _ = self.jabraConnected
        self.read_audio_sample()

    def reIntializeSound(self):
        # workaround for stale read by query_devices
        # https://github.com/spatialaudio/python-sounddevice/issues/125#issuecomment-372281215
        sd._terminate()
        sd._initialize()

    def read_audio_sample(self):
        # Read file to get buffer                                                                                               
        ifile = wave.open("jabra-fade-in-disabler/assets/audio_sample.wav")
        samples = ifile.getnframes()
        audio = ifile.readframes(samples)

        # Convert buffer to float32 using NumPy                                                                                 
        audio_as_np_int16 = np.frombuffer(audio, dtype=np.int16)
        audio_as_np_float32 = audio_as_np_int16.astype(np.float32)

        # Normalise float32 array so that values are between -1.0 and +1.0                                                      
        max_int16 = 2**15
        self.audio_sample = audio_as_np_float32 / max_int16

    @property
    def jabraConnected(self):
        self.reIntializeSound()
        devices = sd.query_devices()
        try:
            jabra_output_device = next(item for item in devices if "Jabra" in item["name"] and item["max_output_channels"] > 0)
            # self.sample_rate = int(jabra_output_device['default_samplerate'])
            return True
        except Exception:
            return False

    def play_audio(self):
        print("*** playing audio")
        sd.play(self.audio_sample, loop=True)
        self.audio_stream_enabled = True

    def stop_audio(self):
        print("*** stopping audio")
        sd.stop()
        self.audio_stream_enabled = False

    @property
    def audioStreamEnabled(self):
        return self.audio_stream_enabled

    # def generate_audio_sample(self):
    #     low_freq = 1 # Hz
    #     duration = 60 # seconds
    #     amplitude = 0.01
    #     lin_sample = np.linspace(0, duration, duration * self.sample_rate, False)
    #     # sine wave
    #     self.audio_sample = amplitude * np.sin(low_freq * lin_sample * 2 * np.pi)
    #     print(self.audio_sample)
    #     # normalize to 16-bit range
    #     self.audio_sample *= 32767 / np.max(np.abs(self.audio_sample))
    #     # convert to 16-bit data
    #     self.audio_sample = self.audio_sample.astype(np.int16)
