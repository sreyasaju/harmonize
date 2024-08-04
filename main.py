from record import record_audio
from midi import convert_to_midi
from playback import play_wav_file, play_midi_file

def main_menu():
    wave_output_file = None
    midi_output = None

    while True:
        print("\n Voice to MIDI Converter")
        print("1. Record your Voice!")
        print("2. Play Recorded Voice")
        print("3. Convert Audio to MIDI")
        print("4. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            record_seconds = int(input("Enter the duration for recording (in seconds): "))
            wave_output_file = input("Enter output filename (e.g., recording.wav): ")
            record_audio(record_seconds, wave_output_file)
        elif choice == '2':
            if wave_output_file is None:
                print("No recorded audio file available!")
                continue
            play_wav_file(wave_output_file)
        elif choice == '3':
            if wave_output_file is None:
                print("You need to record audio first!")
                continue
            midi_output = input("Enter output MIDI filename (e.g., output.midi): ")
            convert_to_midi(wave_output_file, midi_output)
        elif choice == '4':
            print("Exiting Program.")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main_menu()
