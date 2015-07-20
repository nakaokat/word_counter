# -*- coding: utf-8 -*-

ignore = "a the be is are he she they it to"
no_ignore = ""

def main(text, ignore):
    """
    text: str
    ignore: str
    return: dict
    """
    words = text.split(" ")
    ignore_words = ignore.split(" ")
    result = {}
    for word in words:
        if word not in ignore_words and word not in result:
            result[word] = 1
        elif word not in ignore_words and word in result:
            result[word] += 1

    return result
