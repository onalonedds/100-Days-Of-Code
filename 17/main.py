from Quiz import Quiz

questions_1 = [
    ("1. A slug's blood is green.", True),
    ("2. The loudest animal is the African Elephant.", False),
    ("3. Approximately one quarter of human bones are in the feet.", True),
    ("4. The total surface area of a human lungs is the size of a football pitch.", True),
    ("5. In West Virginia, if you accidentally hit an animal with your car, you are free to take it home to eat.", True),
    ("6. In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", False)
]

questions_2 = [
    ("7. It is illegal to pee in the Ocean in Portugal.", True),
    ("8. You can lead a cow down stairs but not up stairs.", False),
    ("9. Google was originally called 'Backrub'.", True),
    ("10. Buzz Aldrin's mother's maiden name was 'Moon'.", True),
    ("11. No piece of square dry paper can be folded in half more than 7 times.", False),
    ("12. A few ounces of chocolate can kill a small dog.", True)
]

quiz = Quiz(questions_1)
quiz.start()
quiz.add_questions(questions_2)
quiz.start()
