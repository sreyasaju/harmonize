# harmonize

![preview.png](assets/preview.png)

> Under development!

harmonize is a voice-to-MIDI python App to convert any human voice recording to MIDI tracks.
This uses `librosa` and `mido` for audio analysis and pitch detection, `PyAudio` for recording and `pydub` for playback tasks.
It is designed to minimally convert  vocal sounds into MIDI data for use in various musical applications.

## Features
- Live Audio Recording: Capture vocal input directly through the application.
- Pitch Detection: Analyze vocal pitch and convert it into MIDI notes.
- MIDI File Generation: Save the detected pitches as MIDI files.

## Installation:

Clone the repository:

```bash
git clone https://github.com/sreyasaju/harmonize.git
cd harmonize
```

Setup a Virtual Environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

Install dependencies:
```bash
pip install -r requirements.txt
```
Run the script: 
```bash
python3 main.py
```
## Usage 

1. Input the parameters: Enter the filename for saving the voice and the MIDI file 
2. Start Recording!
3. Play and hear your voice
4. Convert to MIDI
5. Listen the MIDI file in your favorite audio editor!

## Contributing
Contributions are welcome! Please submit a pull request or open an issue to discuss potential improvements.
Add do star the repo ⭐️


## License
This project is licensed under the MIT License - see the LICENSE file for details.


<hr>
Copyright © 2024 Sreya Saju

