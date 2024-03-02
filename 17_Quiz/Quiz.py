class Quiz:
    def __init__(self, data):
        self._questions = data
        self.size = len(self._questions)
        self._more_questions_were_added = False
        self.score = 0
        self._last_answered_question = 0
        self.start_from_newest = False

    def add_questions(self, data):
        if len(data) > 0:
            self._questions.extend(data)
            self.size = len(self._questions)
            self._more_questions_were_added = True

    @staticmethod
    def _check_answer(answer):
        if answer == "":
            return True
        else:
            return False

    def start(self, start_from_newest=False):
        self.start_from_newest = start_from_newest
        if self._more_questions_were_added and self.start_from_newest:
            print("\nThere are more questions for you!")
        else:
            print("\nWelcome to Quiz!\nPress 'Enter' if you agree, otherwise type any char then 'Enter'.")

        if self.start_from_newest:
            start = self._last_answered_question
        else:
            start = 0
            self.score = 0

        for question in self._questions[start:]:
            answer = input(f"\n{question[0]}")
            if self._check_answer(answer) == question[1]:
                self.score += 1
                print(f"Right! Your score is {self.score}/{len(self._questions)}")
            else:
                print(f"Wrong. It is {question[1]}. Your score is {self.score}/{len(self._questions)}")

        self._last_answered_question = len(self._questions)
