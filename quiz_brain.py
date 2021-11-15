import html

class QuizBrain:

    def __init__(self, q_list):
        """Create a new quiz machine based on a question list"""
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self) -> bool:
        """Check if there are still questions on the list"""
        return self.question_number < len(self.question_list)

    def next_question(self) -> str:
        """Get next question from the list"""
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text} (True/False)"

    def check_answer(self, user_answer: str) -> bool:
        """Check if the player's answer is correct"""
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False


