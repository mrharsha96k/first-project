import pyttsx3

engine = pyttsx3.init()

# Set voice (optional)
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)  # 0 = male, 1 = female (depends on your system)
engine.setProperty("rate", 170)            # speed of speech
engine.setProperty("volume", 1.0)          # volume level

text = """
Hello, everyone. I am JARVIS — your personal AI assistant.
Designed to make your digital life faster, smarter, and effortless.
I can manage your tasks, answer your questions, and assist you anytime.
My purpose is simple — to help you achieve more.
Welcome to a smarter world, powered by JARVIS.
"""

engine.say(text)
engine.runAndWait()
