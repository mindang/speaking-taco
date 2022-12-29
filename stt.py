# import library
import speech_recognition as sr

def sst_function():
    # Initialize recognizer class (for recognizing the speech)
    r = sr.Recognizer()

    # Reading Audio file as source
    # listening the audio file and store in audio_text variable

    with sr.AudioFile('test.wav') as source:
        audio_text = r.listen(source)
        # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
        try:
            # using google speech recognition
            # Adding french langauge option
            text = r.recognize_google(audio_text, language="ko_KR",show_all=False)
            #print('Converting audio transcripts into text ...')
            return text

        except:
            print()
            print('Sorry.. run again...')