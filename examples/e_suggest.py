import re
import os.path

from spyll.hunspell.dictionary import Dictionary
from spyll.hunspell.algo import permutations as pmt
from spyll.hunspell.algo import ngram_suggest, suggest

dic = Dictionary.from_files('tests/fixtures/hunspell-orig/opentaal_forbiddenword1')

# print(list(pmt.permutations('rotten-day', use_dash=True)))
# print([sug for sug in pmt.twowords('rottenday', use_dash=True) if type(sug) == tuple])

# print(dic.roots())
# pms = list(pmt.permutations('permenant', aff=dic.aff))
# print('permanent' in pms)
# print(list(dic.suggest('permenant')))
# print(list(ngram_suggest.ngram_suggest(dic, 'permenant', maxdiff=dic.aff.maxdiff, onlymaxdiff=dic.aff.onlymaxdiff)))

# print([*dic.analyzer.analyze('Foobaz')])
# print(list(dic.suggester.suggest_debug('Brasillian')))
# print(dic.lookup('-vacation'))
print(list(dic.suggester.suggest_debug('foowordbar')))
