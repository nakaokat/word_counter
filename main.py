# -*- coding: utf-8 -*-

class Main:
    def __init__(self, text):
        self.original = text
        self.mark_removed_text = self.remove_mark(text)
        self.words = self.mark_removed_text.split(" ")
        self.output = {}
        self.ignore_words = []


    def remove_mark(self, text):
        """
        :param text:
        :return: str, text that marks is removed.
        """
        words = text.split(" ")
        new_words = []
        for word in words:
            if len(word) > 0:
                last = word[-1]
                if last == "." or last == "," or last == ":" or last == ";":
                    new_words.append(word[0:-1])
                else:
                    new_words.append(word)

        return " ".join(new_words)


    def output(self):
        """
        :return: dict
        """
        result = {}
        for word in self.words:
            if word not in self.ignore_words and word not in result:
                result[word] = 1
            elif word not in self.ignore_words and word in result:
                result[word] += 1

        return result


    def get_original(self):
        """

        :return: str
        """
        return self.original


    def get_words(self):
        """
        :return: list
        """
        return self.words


    def set_ignore_words(self, ignore_words):
        """
        :param ignore_words:
        :return: none
        """
        self.ignore_words = ignore_words


    def get_ignore_words(self):
        """
        :return: list
        """
        return self.ignore_words

    def get_output(self):
        """

        :return:
        """
        result = {}
        for word in self.words:
            if word not in self.ignore_words and word not in result:
                result[word] = 1
            elif word not in self.ignore_words and word in result:
                result[word] += 1

        return result

    def get_order(self):
        result = []
        for word in self.words:
            if word not in self.ignore_words and word not in result:
                result.append(word)
        return result
