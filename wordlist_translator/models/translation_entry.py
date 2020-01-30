'''
custom typings
'''

from typing import TypedDict, List


class TranslationEntry(TypedDict):
    '''
    Custom type for translated items
    '''
    subject: str
    translations: List[str]
