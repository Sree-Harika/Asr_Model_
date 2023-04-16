import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

def getLanguage(argument):
    switcher = {
        1: "en-IN",
        2: "kn-IN"
    }
    return switcher.get(argument, 0)
def getSelection():
    while True:
        try:
            userInput = int(input())
            if (userInput<1 or userInput>2):
                print("Not an integer! Try again.")
                continue
        except ValueError:
            print("Not an integer! Try again.")
            continue
        else:
            return userInput
            break
# Reading Audio file as source
# listening the audio file and store in audio_text variable
def startConvertion(path = 'kannadamod.wav',lang = 'en-IN'):
    with sr.AudioFile(path) as source:
        print('Fetching File')
        audio_text = r.listen(source)
        # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
        try:
        
            # using google speech recognition
            print('Converting audio transcripts into text ...')
            text = r.recognize_google(audio_text, language = lang)
            print(text)
    
        except:
            print('Sorry.. run again...')
if __name__ == '__main__':
    # we can add selection langauges in a list and we can show 'n number of language options to the user by using loop
    print('Please Select Language for Translate : ')
    print('1. English')
    print('2. Kannada')
    # getting language for translating audio to text
    languageSelection = getLanguage(getSelection())
    # calling startConvertion method to start process
    startConvertion("kannadamod.wav",languageSelection) # for time being I am using static file name here, we can take file input from user