# -*- coding: utf-8 -*-

ignore = "a the be is are he she they it to"
no_ignore = ""

def main(text, ignore):
    """
    text: str
    ignore: str
    return: dict
    """
    mark_removed_text = remove_mark(text)
    words = mark_removed_text.split(" ")
    ignore_words = ignore.split(" ")
    result = {}
    for word in words:
        if word not in ignore_words and word not in result:
            result[word] = 1
        elif word not in ignore_words and word in result:
            result[word] += 1

    return result


def order(text, ignore):
    """
    :param text:
    :param ignore:
    :return: list which is ordered
    this is used to order a dictionary of counter.
    """
    mark_removed_text = remove_mark(text)
    words = mark_removed_text.split(" ")
    ignore_words = ignore.split(" ")
    result = []
    for word in words:
        if word not in ignore_words and word not in result:
            result.append(word)
    return result

def remove_mark(text):
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

class Main:
    def __init__(self, text):
        self.original = text
        self.words = text.split(" ")
        self.output = {}


    def remove_mark(self):
        """
        words リストから、語尾が句読点のものを探してそれをとる
        :return: none
        """
        new_words = []
        for word in self.words:
            if len(word) > 0:
                last = word[-1]
                if last == "." or last == "," or last == ":" or last == ";":
                    new_words.append(word[0:-1])
                else:
                    new_words.append(word)
        self.words = new_words