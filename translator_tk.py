# Libraries Used
# For GUI
from tkinter import *
from tkinter import filedialog
# For Translation
from googletrans import Translator
# For Audio
import pyttsx3

# GUI Creation
window = Tk()
window.title("Language Translator ___RSP___")
window.geometry('640x480+100+100')
window.configure(bg='#FD7272')

# Initialising Translator and Speech Engine
translator = Translator()
engine = pyttsx3.init()
engine.setProperty("rate", 150)

Post_lang_Choice = StringVar()
# Setting a default Language for Translation
Post_lang_Choice.set('hindi')
# Creating a dictionary for the set of Languages available
lang = {'af': 'afrikaans', 'sq': 'albanian', 'am': 'amharic', 'ar': 'arabic', 'hy': 'armenian', 'az': 'azerbaijani',
        'eu': 'basque', 'be': 'belarusian', 'bn': 'bengali', 'bs': 'bosnian', 'bg': 'bulgarian', 'ca': 'catalan',
        'ceb': 'cebuano', 'ny': 'chichewa', 'zh-cn': 'chinese (simplified)', 'zh-tw': 'chinese (traditional)',
        'co': 'corsican', 'hr': 'croatian', 'cs': 'czech', 'da': 'danish', 'nl': 'dutch', 'en': 'english',
        'eo': 'esperanto', 'et': 'estonian', 'tl': 'filipino', 'fi': 'finnish', 'fr': 'french', 'fy': 'frisian',
        'gl': 'galician', 'ka': 'georgian', 'de': 'german', 'el': 'greek', 'gu': 'gujarati', 'ht': 'haitian creole',
        'ha': 'hausa', 'haw': 'hawaiian', 'iw': 'hebrew', 'he': 'hebrew', 'hi': 'hindi', 'hmn': 'hmong',
        'hu': 'hungarian', 'is': 'icelandic', 'ig': 'igbo', 'id': 'indonesian', 'ga': 'irish', 'it': 'italian',
        'ja': 'japanese', 'jw': 'javanese', 'kn': 'kannada', 'kk': 'kazakh', 'km': 'khmer', 'ko': 'korean',
        'ku': 'kurdish (kurmanji)', 'ky': 'kyrgyz', 'lo': 'lao', 'la': 'latin', 'lv': 'latvian', 'lt': 'lithuanian',
        'lb': 'luxembourgish', 'mk': 'macedonian', 'mg': 'malagasy', 'ms': 'malay', 'ml': 'malayalam', 'mt': 'maltese',
        'mi': 'maori', 'mr': 'marathi', 'mn': 'mongolian', 'my': 'myanmar (burmese)', 'ne': 'nepali', 'no': 'norwegian',
        'or': 'odia', 'ps': 'pashto', 'fa': 'persian', 'pl': 'polish', 'pt': 'portuguese', 'pa': 'punjabi',
        'ro': 'romanian', 'ru': 'russian', 'sm': 'samoan', 'gd': 'scots gaelic', 'sr': 'serbian', 'st': 'sesotho',
        'sn': 'shona', 'sd': 'sindhi', 'si': 'sinhala', 'sk': 'slovak', 'sl': 'slovenian', 'so': 'somali',
        'es': 'spanish', 'su': 'sundanese', 'sw': 'swahili', 'sv': 'swedish', 'tg': 'tajik', 'ta': 'tamil',
        'te': 'telugu', 'th': 'thai', 'tr': 'turkish', 'uk': 'ukrainian', 'ur': 'urdu', 'ug': 'uyghur', 'uz': 'uzbek',
        'vi': 'vietnamese', 'cy': 'welsh', 'xh': 'xhosa', 'yi': 'yiddish', 'yo': 'yoruba', 'zu': 'zulu'}

# Putting language values (not the symbol) into the list
languages = []
for langs in lang.values():
    languages.append(langs)


# Function for Exception of non entry of text
def exc():
    print("Please Enter text first")
    engine.say("Please Enter text first")
    engine.runAndWait()


# Function for Selecting the text File
def TF():
    print("Selecting File....")
    text_file = filedialog.askopenfilename(initialdir=r"C:\Users\Rahul Roy\PycharmProjects\GIT\NLP",
                                           title="Select a text File to be translated",
                                           filetypes=(("text files", "*.txt"), ("all file", "*.*")))
    print(text_file)

    with open(text_file) as text:
        contents = text.read()
        print(contents)
        InputVar.set(contents)
        text.close()


# Function for Pronounciating the text
def Pronounce():
    try:
        key_list = list(lang.keys())
        val_list = list(lang.values())
        end_lan = Post_lang_Choice.get()
        end_position = val_list.index(end_lan)
        ep = key_list[end_position]
        translator.translate(InputVar.get(), dest=ep)
        trans = translator.translate(InputVar.get(), dest=ep)
        if trans.pronunciation is not None:
            print(trans.pronunciation)
            engine.say(trans.pronunciation)
            engine.runAndWait()
        else:
            # engine.say("I can't pronounce it properly, but still i'll say")
            print(trans.text)
            engine.say(trans.text)
            engine.runAndWait()
    except:
        exc()


# Function for Translating the text
def Translate():
    try:
        key_list = list(lang.keys())
        val_list = list(lang.values())
        end_lan = Post_lang_Choice.get()
        end_position = val_list.index(end_lan)
        ep = key_list[end_position]
        print(ep)
        trans = translator.translate(InputVar.get(), dest=ep)
        print(trans)
        Label(window, text="Translated Text", font=('Helvetica', 12),
              bg='black', fg='white').place(x=20, y=190)
        Label(window, text=trans.text, font=("MS Serif Bold", 16)
              , fg='white', bg='#4b4b4b').place(x=30, y=220)
    except:
        exc()


# Creating OptionMenu, Labels and Buttons on the Window for ease
Post_lang_Menu = OptionMenu(window, Post_lang_Choice, *languages)
Post_lang_Menu.config(bg='#EAB543')
Post_lang_Label = Label(window, text="Choose Translate Language",
                        font=('System', 12)).place(x=390, y=30)
Post_lang_Menu.place(x=500, y=60)

Input_lang_Label = Label(window, text="Enter Text below",
                         font=('System', 16), bg='#FD7272').place(x=50, y=100)
InputVar = StringVar()
Input_TextBox = Entry(window, textvariable=InputVar, width=50,
                      font=('Georgia', 14)).place(x=30, y=120)

Text_Button = Button(window, text="Have a text file? Select now.", command=TF,
                     font=('Verdana', 10, 'underline'), borderwidth=0,
                     bg='#FD7272', relief=GROOVE).place(x=220, y=150)

Translate_Button = Button(window, text='Translate', command=Translate, bg='#c56cf0', fg='white',
                          font=('Great Vibes', 14), relief=GROOVE).place(x=280, y=300)

Pronounce_Button = Button(window, text='Pronounce Translated Text', font=('Century', 12),
                          bg='#1B9CFC', fg='white', command=Pronounce, relief=GROOVE).place(x=230, y=350)

window.mainloop()

