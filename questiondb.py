import requests
from question_model import Question


class QuestionBank:
    def __init__(self):
        self.parameters = {"amount": 10,
                           "type": "boolean"}
        self.response = requests.get(url="https://opentdb.com/api.php", params=self.parameters)
        self.response.raise_for_status()
        data = self.response.json()
        self.question_data = data["results"]
        self.questions = []
        for question in self.question_data:
            question_text = question["question"]
            question_answer = question["correct_answer"]
            new_question = Question(question_text, question_answer)
            self.questions.append(new_question)
