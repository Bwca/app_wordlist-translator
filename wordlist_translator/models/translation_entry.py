from typing import TypedDict, List


class TranslationEntry(TypedDict):
    subject: str
    translations: List[str]
