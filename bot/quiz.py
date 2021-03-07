import asyncio
import os, sys
import random
import question

class Quiz:
    
    def __init__(self, client):
        self.client = client
        self.questions = []
        self.current = None
        self.tries = 3
        self.lives = 5
        self.score = 0
        self.wins = 10
        self.started = False
        
        data = os.listdir('bot/quiz_data')
        working_dir = os.getcwd() + '/bot/quiz_data' + os.path.sep
        for file in data:
            filepath = working_dir + file
            print("loading..." + filepath)
            self.load_questions(filepath)
        print("Quiz loading done")

    async def start(self, channel):
        self.started = True
        await channel.send("Quiz starting in 5 seconds")
        await asyncio.sleep(5)
        await self.ask_question(channel)
    
    def load_questions(self, filepath):
        quizfile = open(filepath, "r")
        for line in quizfile:
            content = line.split(":")
            q = question.Question(content)
            self.questions.append(q)

    async def ask_question(self, channel):
        self.tries = 3
        self.current = self.questions[random.randint(0, len(self.questions) - 1)]
        await channel.send('Question: {}'.format(self.current.question))
    
    async def stop(self, channel):
        if self.lives < 1:
            await channel.send("You lost :(")
        elif self.score >= 10:
            await channel.send("CONGRATS! You won!")
        self.started = False

    async def answer_question(self,message):
        finished = False
        if (not finished):
            if (self.started and self.current is not None):
                if (self.current.is_correct(message.content)):
                    await message.channel.send("YOU GOT IT CORRECT")
                    finished = True
                    self.score += 1
                    if (self.score >= 10):
                        self.stop(message.channel)
                else:
                    self.tries -= 1
                    if (self.tries < 1):
                        finished = True
                        self.lives -= 1
                        await message.channel.send("You ran out of tries. The answer was : {} \nLives Left: {}"
                                                    .format(self.current.answer, self.lives))
                        if (self.lives < 1):
                            await self.stop(message.channel)
                    else:
                        await message.channel.send("Wrong :( You have {} tries left".format(str(self.tries)))
        if (finished and self.lives > 0 and self.score < 10):
            await message.channel.send("Score: {}".format(self.score))
            await message.channel.send("Next question...")
            await self.ask_question(message.channel)
    
    