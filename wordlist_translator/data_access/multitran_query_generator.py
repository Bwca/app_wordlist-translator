def generate_multitran_translation_query(word: str, source_language_id=1, target_language_id=2) -> str:
    '''
    generate a query to m.exe on multitran.com
    language params:
    1= English; 2= Russian
    query link: https://www.multitran.com/m.exe
    params:
        l1: source language id
        l2: target language id
        s: item to translate
    '''
    return "https://www.multitran.com/m.exe?l1={0}&l2={1}&s={2}".format(source_language_id, target_language_id, word)
