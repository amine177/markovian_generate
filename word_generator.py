#!/bin/env python3
# -*- coding: utf-8 -*-


import random
import sys


class LearningList:

    def __init__(self):

        self.scores = {}

    def addItem(self, parent, word):

        if parent in self.scores:
            if word in self.scores[parent]:
                self.scores[parent][word] += 1
            else:
                self.scores[parent][word] = 1
        else:
            self.scores[parent] = {}
            self.scores[parent][word] = 1

    def learn(self, text):

        words = text.split()
        prev = ""

        for i in words:
            self.addItem(prev, i)
            prev = i

    def pickOne(self, parent):

        if parent in self.scores:
            vl = list(self.scores[parent].values())
            element_score = vl[int(random.random() * len(vl))]
            for i, j in self.scores[parent].items():
                if j >= element_score:
                    return i
        else:
            return ""

    def reset(self):
        self.scores.clear()


class Writer:

    def __init__(self, l, fp):
        self.lst = l
        self.file = open(fp, 'r')
        while True:
            text = self.file.readline()
            if text:
                text = text[:-1]
                if text:
                    l.learn(text)
            else:
                break

    def write(self, n):

        res = ""
        prv = ""
        for i in range(n):
            word = self.lst.pickOne(prv)
            res = res + " " + word
            prv = word

        return res


if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Usage: python word_generator.py learning_file number_lines")
        sys.exit(1)
    else:
        f = sys.argv[1]
        n = int(sys.argv[2])

    gen = LearningList()
    writer = Writer(gen, f)
    print(writer.write(n))
