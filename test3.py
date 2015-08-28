# -*- coding: utf-8 -*-
__author__ = 'nakaokataiki'

from main import Main

main = Main("foo bar hoge hoge hoge.")

print(main.get_words())

main.set_ignore_words(["bar"])

print(main.get_ignore_words())

print(main.get_original())

print(main.get_output())

print(main.get_order())