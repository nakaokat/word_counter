# -*- coding: utf-8 -*-
__author__ = 'nakaokataiki'

from main import Main

main = Main("foo bar hoge hoge")

print(main.get_words())

main.set_ignore_words(["bar"])

print(main.get_ignore_words())

print(main.get_original())