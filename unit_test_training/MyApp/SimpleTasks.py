import os

class SimpleTasks(object):

    def get_greeting(self, greeting):
        my_username = os.environ['USERNAME']
        full_greeting =  greeting + ", " + my_username +"!"
        return full_greeting

    def get_sum(self, x, y):
        return x+y