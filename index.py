pip install nltk
import nltk
import re
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')
stop_words = set(stopwords.words('english'))

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from collections import defaultdict

ps = PorterStemmer()
lemmatizer = WordNetLemmatizer()

doc1 = "Television is a wonderful scientific gift. It combines the advantages of cinema and radio. The most important and effective form of entertainment is television."
doc2 = "Everyone knows that paper is made from trees. But when one looks at trees, one cannot imagine that something so soft and fragile as the paper is made is so hard and strong. Plant materials such as wood are made of fibres known as cellulose."
doc3 = "Yesterday I saw a film titled Macbeth. Its story elements are interesting. The film’s hero, Macbeth, assassinates Duncan and a

docs = [doc1, doc2, doc3]

token1 = word_tokenize(doc1)
token2 = word_tokenize(doc2)
token3 = word_tokenize(doc3)

term = token1+token2+token2


LowerCaseone = []
LowerCasetwo = []
LowerCasethree = []
for i in token1 :
    LowerCaseone.append(i.lower())
for i in token2 :
    LowerCasetwo.append(i.lower())
for i in token3 :
    LowerCasethree.append(i.lower())


Remove_stopWordsone = []
Remove_stopWordstwo = []
Remove_stopWordsthree = []
for i in LowerCaseone:
    if i not in stop_words:
        Remove_stopWordsone.append(i)
for i in LowerCasetwo:
    if i not in stop_words:
        Remove_stopWordstwo.append(i)
for i in LowerCasethree:
    if i not in stop_words:
        Remove_stopWordsthree.append(i)


Stemmingone = []
Stemmingtwo = []
Stemmingthree = []
Stemmingfour = []
for x in Remove_stopWordsone:
    Stemmingone.append(ps.stem(x))
for y in Remove_stopWordstwo:
    Stemmingtwo.append(ps.stem(y))
for z in Remove_stopWordsthree:
    Stemmingthree.append(ps.stem(z))


final_term = Stemmingone+Stemmingtwo+Stemmingthree

for x in final_term:
    words = [re.sub(r'[^a-zA-Z0-9]+', '', word) for word in final_term]
    
for x in words:
   final_process = list(set(words))
  
  
final_processtwo = []
for x in final_process:
    if x!= '':
        final_processtwo.append(x)
      
      

final_processtwo = sorted(final_processtwo)
tdim = [[] for i in range(len(final_processtwo))]
for i in range(len(final_processtwo)):
    tdim[i].append(final_processtwo[i])
    if final_processtwo[i] in Stemmingone:
        tdim[i].append(1)
    else: 
        tdim[i].append(0)
    if final_processtwo[i] in Stemmingtwo:
        tdim[i].append(1)
    else: 
        tdim[i].append(0)
    if final_processtwo[i] in Stemmingthree:
        tdim[i].append(1)
    else: 
        tdim[i].append(0)
    
  
print(" word, Doc1, Doc2, Doc3")
print(tdim)
