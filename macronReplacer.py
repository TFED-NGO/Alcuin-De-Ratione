replacer = {
    'e' : ['E1', 'E2'],
    'a' : ['A1', 'A2'],
    's' : ['S1', 'S2']
}

def replaceMacrons(text):
    return f'<g ref=\"#{replacer[text][0]}">{replacer[text][1]}</g>'

def run():
    original = open('edition.xml', mode='r', encoding='utf-8', errors='xmlcharrefreplace')
    output = open('glyphs_in_need_of_definition.txt', mode='w', encoding='utf-8', errors='xmlcharrefreplace')

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
        text = text[:i] + f'[{text[i]}]' + text[macron_index + 9:]
        macron_index = text.find("<macron/>")
        preview = text[i-10:i + 15].replace("\n", "")
        output.write(f'{char_of_interest} in context: "...{preview}..."\n')

    original.close()
    output.close()

if __name__=="__main__":
    run()
