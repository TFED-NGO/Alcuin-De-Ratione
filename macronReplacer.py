charDecl = ""

replacer = {
    'e': 'ē',
    'a': 'ā',
    'i': 'ī',
    'o': 'ō',
    'u': 'ū',
    'E': 'Ē',
    'A': 'Ā',
    'I': 'Ī',
    'O': 'Ō',
    'U': 'Ū',
}

def buildGRef(text):
    return f'<g ref="#{text}_macron"/>'

def declareCharacter(char):
    global charDecl
    global replacer
    replacer[char] = buildGRef(char)
    charDecl += f'\n    <char xml:id="{char}_macron">\n        <unicodeProp name="Canonical_Combining_Class" value="230"/>\n        <localProp name="name"\n            value="{str.upper(char)} CHARACTER WITH A MACRON OVER IT"/>\n        <mapping type="standard">{char}&#x00AF;</mapping>\n    </char>'

def replaceMacrons(text):
    global charDecl
    global replacer
    if (text not in replacer):
        declareCharacter(text)
    return f'{replacer[text]}'

def run():
    global charDecl
    global replacer
    original = open('edition.xml', mode='r', encoding='utf-8', errors='xmlcharrefreplace')
    output = open('edition_fixed.xml', mode='w', encoding='utf-8', errors='xmlcharrefreplace')

    text = original.read()

    macron_index = text.find("<macron/>")
    while (macron_index != -1):
        i = macron_index - 1
        while ((not text[i].isalpha()) and i >= 0):
            i -= 1
        char_of_interest = text[i]
        e = ''
        try:
            e = replaceMacrons(char_of_interest)
        except KeyError:
            e = f"[{char_of_interest}]"
        text = text[:i] + e + text[macron_index + 9:]
        macron_index = text.find("<macron/>")
    char_decl_index = text.find("<charDecl>")
    text = text[:char_decl_index + 10] + charDecl + text[char_decl_index + 10:]
    
    output.write(text)

    original.close()
    output.close()

if __name__=="__main__":
    run()
