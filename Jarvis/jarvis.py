import pyttsx3
import speech_recognition as sr
from datetime import datetime
import webbrowser

# pyttsx3 엔진 초기화
engine = pyttsx3.init()

now = datetime.now()
current_time = now.strftime("%I:%M %p")  # 초 제외, AM/PM 형식으로 현재 시간 저장

# 사용 가능한 음성 목록 확인
voices = engine.getProperty('voices')
desired_voice = None
for voice in voices:
    if voice.name == "Microsoft Zira Desktop - English (United States)":
        desired_voice = voice
        break

# 원하는 영어 음성이 있는 경우 설정
if desired_voice:
    engine.setProperty('voice', desired_voice.id)
else:
    print("Desired English voice not found. Using default voice.")

# 음성 속도 조절
engine.setProperty('rate', 200)

# 인사 음성 출력
greeting = f"Good morning, it's {current_time}. I am Jarvis sir, Please tell me how may I help you."
print(greeting)
engine.say(greeting)
engine.runAndWait()

# 열 사이트 목록
websites = [
    'https://www.google.com',
    'https://www.youtube.com',
    # 다른 웹사이트도 추가 가능
]

def takecommand():
    command = sr.Recognizer()
    while True:  # 무한 루프로 계속 명령을 인식하도록 설정
        with sr.Microphone() as source:
            print("Listening....")
            command.adjust_for_ambient_noise(source)
            command.pause_threshold = 1
            audio = command.listen(source)

        try:
            print("Recognizing....")
            query = command.recognize_google(audio, language="en-in")
            print("You said:", query)

            if 'what time is it' in query:
                engine.say(f"The current time is {current_time}.")
                engine.runAndWait()
                engine.say("Do you have any other work?")

            if 'open Google' in query:
                engine.say("Confirm")
                webbrowser.open('https://www.google.com')
                engine.runAndWait()
                engine.say("Do you have any other work?")

            if 'open YouTube' in query:
                engine.say("Confirm")
                webbrowser.open('https://www.youtube.com')
                engine.runAndWait()
                engine.say("Do you have any other work?")

            if 'execute them all' in query:
                engine.say("Execute them all operation")
                execute_all()
                engine.runAndWait()
                engine.say("Do you have any other work?")
                
            if 'searching' in query:
                search_query = query.split('searching', 1)[1].strip()
                engine.say(f"Ok, Searching on Google for {search_query}")
                search_google(search_query)
                engine.runAndWait()
                engine.say("Do you have any other work?")
            
            if 'turn off Jarvis' in query:
                engine.say("Turning off Jarvis, bye bye")
                engine.runAndWait()
                break  # 루프 종료하여 프로그램 종료

        except Exception as Error:
            engine.runAndWait()

def execute_all():
    # 모든 웹사이트 실행
    for website in websites:
        webbrowser.open(website)

def search_google(query):
    search_url = f"https://www.google.com/search?q={query}"
    webbrowser.open(search_url)

takecommand()