from quiz_brain_question_model import Question
from quiz_brain_ui import *
from quiz_brain import QuizBrain
import requests
para= {
    "amount":10,
    "type":"boolean"}

response=requests.get(url="https://opentdb.com/api.php",params=para)
response.raise_for_status()
data=response.json()
question_bank = []

for question in data['results']:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
ui = UserInterface(quiz)
