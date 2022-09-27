'''
este codigo é fixe quando queremos converted um texto para letra escrita a mao
'''


import pywhatkit
text = '''
Para proxima vez tenta nao demorar muito tempo
'''

pywhatkit.text_to_handwriting(text,
                             rgb=(1,0,255),
                            save_to='handwrite.png')
print('converted...')