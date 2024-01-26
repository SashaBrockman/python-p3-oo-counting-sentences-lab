#!/usr/bin/env python3
import ipdb

class MyString:
    def __init__(self, value = ""):
        self.value = value

    @property
    def value(self):
        """The value property"""
        return self._value

    @value.setter
    def value(self, value):
        """value must be a string"""
        if(type(value) == str):
            self._value = value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        if(self.value.endswith(".")):
            return True
        else:
            return False

    def is_question(self):
        if(self.value.endswith("?")):
            return True
        else:
            return False

    def is_exclamation(self):
        if(self.value.endswith("!")):
            return True
        else:
            return False

    def count_sentences(self):
        new_sentence = self.value.replace("!", ".")
        new_sentence = new_sentence.replace("?", ".")
        new_sentence = new_sentence.split(".")
        while "" in new_sentence:
            new_sentence.remove("")
        return len(new_sentence)
