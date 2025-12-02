import wave

# Path to your WAV file
wav_file_path = "audio.wav"  # Make sure this file exists in the same folder

try:
    # Open the WAV file in read-binary mode
    with wave.open(wav_file_path, "rb") as wav:
        # Get number of channels
        channels = wav.getnchannels()
        # Get sample/frame rate
        frame_rate = wav.getframerate()
        # Get number of frames
        num_frames = wav.getnframes()
        # Duration in seconds
        duration = num_frames / frame_rate

        print("Channels:", channels)
        print("Frame rate (samples per second):", frame_rate)
        print("Number of frames:", num_frames)
        print("Duration (seconds):", duration)

except FileNotFoundError:
    print(f"File not found: {wav_file_path}")
except wave.Error as e:
    print(f"Error reading WAV file: {e}")

