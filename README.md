# wordlist-translator

Feed it a list of words in foreign language and get a list of their translations with transcriptions. Should be useful for lazy people like me who are very reluctant when it comes to looking up unknown foreign words.

```
python3 ./wordlist_translator/ -m
```

Provide a path to a file with words to translate into Russian, translated results will be stored as json in the results folder. The file with the word list to be translated should contain words separated by news lines, i.e. each word must be on a new line.
