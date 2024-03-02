class Quiz:
    def __init__(self, data):
        self.questions = data
        self.score = 0

    @staticmethod
    def _check_answer(answer):
        if answer == "":
            return True
        else:
            return False

    def start(self):
        self.score = 0
        print("Welcome to Quiz!\nPress 'Enter' if you agree, otherwise type any char then 'Enter'.")

        for question in self.questions:
            answer = input(f"\n{question[0]}")
            if self._check_answer(answer) == question[1]:
                self.score += 1
                print(f"Right! Your score is {self.score}/{len(self.questions)}")
            else:
                print(f"Wrong. It is {question[1]}. Your score is {self.score}/{len(self.questions)}")

        print(f"\nYou've completed the Quiz with score {self.score}/{len(self.questions)}")