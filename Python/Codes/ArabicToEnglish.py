# List Dictionary 31 Keys All Keys


# Letter Arabic and Values Letters English
def ar(in_English):
    Arabic = {
        'ا': 'a',
        'ب': 'b',
        'ت': 't',
        'ث': 'tha',
        'ج': 'j',
        'ح': 'ho',
        'خ': 'k',
        'د': 'd',
        'ذ': 'th',
        'ر': 'r',
        'ز': 'za',
        'س': 'sa',
        'ش': 'sh',
        'ص': 's',
        'ض': 'da',
        'ط': 'ta',
        'ع': 'a',
        'غ': 'gh',
        'ف': 'fa',
        'ق': 'ka',
        'ك': 'k',
        'ل': 'l',
        'م': 'm',
        'ن': 'n',
        'ه': 'h',
        'و': 'w',
        'ي': 'y',
        'ة': 'h',
        'ى': '',
        'آ': 'a',
        'ؤ': 'wa',
        'ئ': 'a',
    }
    val = Arabic.values()
    enlist = list(in_English)
    ListEnglish = []
    for x in enlist:
        d = Arabic.get(x)
        ListEnglish.extend(d)
    joinLetter = ''.join(ListEnglish)
    print("\nEnglish: {} And This Arabic : {}".format(in_English, joinLetter))
ar('القيمة')
