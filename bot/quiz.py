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
        self.wins = 0
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
        self.current = self.questions[random.randint(0, len(self.questions) - 1)]
        await channel.send('Question: {}'.format(self.current.question))
    
    async def stop(self, channel):
        if self.tries < 0:
            await channel.send("You lost!")
        elif self.wins > 2:
            await channel.send("You won!")
        self.started = False

    async def answer_question(self,message):
        if (self.started and self.current is not None):
            if (self.current.is_correct(message.content)):
                await message.channel.send("YOU GOT IT CORRECT")
                self.wins += 1
            else:
                self.tries -= 1
                await message.channel.send("Wrong :( You have {} tries left".format(str(self.tries)))
        await self.ask_question(message.channel)
    
    