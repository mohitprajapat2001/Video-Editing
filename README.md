# Video Editing with Python

Welcome to the Video Editing project! This repository demonstrates how to perform basic video editing tasks using Python and the MoviePy library. You can extract audio from video files, mute audio, and replace audio tracks with different audio files.

## Features

- Extract audio from video files
- Mute the audio of a video
- Replace the audio of a video with a different audio file

## Prerequisites

Make sure you have Python installed on your machine. You will also need to install the MoviePy library. You can install it using pip:

```bash
pip install moviepy
```

## Usage

### CustomClip Class

The `CustomClip` class provides methods to handle video and audio files. Here are the methods available:

- **set_audio_file(file: str, t_start=0, t_end=None)**: Sets an audio file as a clip.
- **set_video_file(file: str, t_start=0, t_end=None)**: Sets a video file as a clip.
- **extract_audio(new_file: str)**: Extracts audio from the video clip and saves it to a new file.
- **write_audio_file(new_file: str)**: Writes the audio clip to a specified file.
- **write_video_file(new_file: str)**: Writes the video clip to a specified file.
- **set_audio(audio_file, new_file)**: Sets a new audio file to the video clip and saves it.

### Notes

- Ensure the video and audio files are in the same directory as your script or provide the full path.
- The `t_start` and `t_end` parameters allow you to specify the portion of the video or audio you want to work with.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE] file for more details.

## Contact

For questions or feedback, feel free to reach out at [mohitdevelopment2001@gmail.com].
