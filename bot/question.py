class Question:
    def __init__(self, content = []):
        self.answer = content[0]
        self.question = content[1]

    def get_answer(self):
        return self.answer

    def is_correct(self, response):
        if (response.lower().strip() == self.answer.lower().strip()):
            return True
        return False