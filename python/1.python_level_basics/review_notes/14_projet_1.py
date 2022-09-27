'''
1. project ira consistir na ciraçao de um cv
        para isso temos de install pip3 - install  python-docx
        import docx
2. Começar por criar alguns paragrafos com informaçao minha como nome,telefone e email

3. 
'''
from  docx import Document

'''funcao document'''
document = Document()

name =  'Luis'
Phone = '918091647'
email = 'dataengineer.developer@gmail.com'

'''concatenar os dados da variaveis que dei anteriormente'''
document.add_paragraph(
    name + ' | ' + Phone + ' | ' + email)


'''salvar as alteraçoes documentos sempre que correr o codigo'''
document.save('cv.docx')


