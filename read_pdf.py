import PyPDF2
import re

def whitespace_ratio(text):
    return len(text.split(' '))/len(text)

def read_pdf(file_name):
    reader = PyPDF2.PdfReader(file_name)
    text = reader.pages[0].extract_text()
    text0 = re.sub("  า"," ำ",text)
    
    if whitespace_ratio(text) > 0.3:
        
        text1 = re.sub("\s{2,}","<WS>",text0)
        text2 = re.sub('(?<=[A-z()])\s(?=[A-z()])',"<WS>",text1)
        text3 = re.sub(" ","",text2)
        text4 = re.sub("<WS>"," ",text3)
        
    else:
        text1 = re.sub(" า","ำ",text0)
        text2 = re.sub('(?<=[A-z()])\s(?=[A-z()])',"<WS>",text1)
        text3 = re.sub("\s{2,}"," ",text2)
        text4 = re.sub("<WS>"," ",text3)
        
    text4 = re.sub(" า","ำ",text4)
    text4 = re.sub(" ้า","้ำ",text4)
    text4 = re.sub("É","่",text4)
    text4 = re.sub("Ê","้",text4)
    text4 = re.sub(" ้า","้ำ",text4)
    final_text = re.sub(" ่า","้่ำ",text4)
    
    
    return final_text