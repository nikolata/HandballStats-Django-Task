import threading
import time
import random
import queue
from .utils import store_info_from_input, order_teams
import logging

BUF_SIZE = 50
q = queue.Queue(BUF_SIZE)


class ProducerThread(threading.Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, verbose=None):
        super(ProducerThread, self).__init__()
        self.target = target
        self.name = name

    def run(self, game):
        if not q.full():
            if game == "stop":
                q.put(game)
                return
            q.put(game)
            time.sleep(random.random())
        else:
            q.put("stop")
            return
        return


class ConsumerThread(threading.Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, verbose=None):
        super(ConsumerThread, self).__init__()
        self.target = target
        self.name = name
        return

    def run(self):
        viewed_teams = []
        teams = []
        while True:
            if not q.empty():
                line = q.get()
                logging.info(line)
                if line == "stop":
                    break
                game = line.split("|")
                first_team = game[0][:-1]
                second_team = game[1][1:-1]
                first_game = game[2]
                second_game = game[3]
                store_info_from_input(first_team, second_team, first_game, second_game, viewed_teams, teams)
                store_info_from_input(second_team, first_team, second_game, first_game, viewed_teams, teams)
                time.sleep(2)
            else:
                time.sleep(3)
        return
