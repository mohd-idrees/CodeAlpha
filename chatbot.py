import nltk
from nltk.chat.util import Chat, reflections
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how are you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello!", "Hey there!", "Hi!"]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created using NLTK.",]
    ],
    [
        r"how are you ?",
        ["I'm doing great, how about you?","Fine!"]
    ],
    [
        r"who are you ?",
        ["I'm just a bunch of code, but thanks for asking!",]
    ],
    [
        r"sorry (.*)",
        ["It's okay, no worries!", "No need to apologize!",]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that!", "Great! How can I assist you today?"]
    ],
    [
        r"what (.*) want ?",
        ["I just want to chat with you!",]
    ],
    [
        r"(.*) created ?",
        ["I was created using Python and NLTK.", "I am the result of coding and creativity!"]
    ],
    [
        r"(.*) (location|city) ?",
        ['I am everywhere.']
    ],
    [
        r"quit",
        ["Bye! Take care.", "Goodbye!"]
    ],
]
def chatbot():
    print("Hi, I'm a chatbot created using NLTK. Let's chat! Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()
if __name__ == "__main__":
    chatbot()