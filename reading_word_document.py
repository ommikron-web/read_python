import docx

def readingtext(filename):
    doc=docx.Document(filename)


    completedtext=[]

    for paragraph in doc.paragraphs:
        completedtext.append(paragraph.text)

    return '\n' .join(completedtext)

texto=readingtext('file.docx')
print(texto)