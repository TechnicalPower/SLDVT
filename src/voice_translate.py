import constants
from gtts import gTTS
from playsound import playsound
from tempfile import TemporaryFile



# directory input changed into string single sentence
def read_dir(dir):
    print("directory is " + dir)
    return open(dir, "r").read()

#tranlating string sentence into words array
def string_to_word(str):
    print(str)
    return str.split()


# Important!! translating the string words into voice with speaker output
def voice_output(out):
    #TODO: Implementation with GTTS 
    for word in out:
        tts = gTTS(word)
        tts.save("buffer.mp3")
        playsound("buffer.mp3")

def main():
    # Debug purpose - starting the python file with satisfied dependencies
    print("""Run the voice translator..
          Checkpoint : 1""")
    
    # Call read directiory and get file input into string
    input_text = read_dir(constants.INPUT_TEST_DIRECTORY)

    # Divide the string words into array elements with each element string
    str_out = string_to_word(input_text)

    voice_output(str_out)
    
    # Return the single line to check for the string words
    print(str_out)





if __name__ == "__main__":
    main()