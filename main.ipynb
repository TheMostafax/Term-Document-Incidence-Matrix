{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 153,
   "id": "8287c21a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: nltk in c:\\users\\mostafa hassan\\anaconda3\\lib\\site-packages (3.7)Note: you may need to restart the kernel to use updated packages.\n",
      "\n",
      "Requirement already satisfied: joblib in c:\\users\\mostafa hassan\\anaconda3\\lib\\site-packages (from nltk) (1.1.0)\n",
      "Requirement already satisfied: tqdm in c:\\users\\mostafa hassan\\anaconda3\\lib\\site-packages (from nltk) (4.64.1)\n",
      "Requirement already satisfied: regex>=2021.8.3 in c:\\users\\mostafa hassan\\anaconda3\\lib\\site-packages (from nltk) (2022.7.9)\n",
      "Requirement already satisfied: click in c:\\users\\mostafa hassan\\anaconda3\\lib\\site-packages (from nltk) (8.0.4)\n",
      "Requirement already satisfied: colorama in c:\\users\\mostafa hassan\\anaconda3\\lib\\site-packages (from click->nltk) (0.4.5)\n"
     ]
    }
   ],
   "source": [
    "pip install nltk"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 154,
   "id": "2cefc5b1",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[nltk_data] Downloading package punkt to C:\\Users\\Mostafa\n",
      "[nltk_data]     Hassan\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]   Package punkt is already up-to-date!\n",
      "[nltk_data] Downloading package stopwords to C:\\Users\\Mostafa\n",
      "[nltk_data]     Hassan\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]   Package stopwords is already up-to-date!\n",
      "[nltk_data] Downloading package wordnet to C:\\Users\\Mostafa\n",
      "[nltk_data]     Hassan\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]   Package wordnet is already up-to-date!\n",
      "[nltk_data] Downloading package omw-1.4 to C:\\Users\\Mostafa\n",
      "[nltk_data]     Hassan\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]   Package omw-1.4 is already up-to-date!\n"
     ]
    }
   ],
   "source": [
    "import nltk\n",
    "import re\n",
    "nltk.download('punkt')\n",
    "nltk.download('stopwords')\n",
    "nltk.download('wordnet')\n",
    "nltk.download('omw-1.4')\n",
    "stop_words = set(stopwords.words('english'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 155,
   "id": "9a1c27bd",
   "metadata": {},
   "outputs": [],
   "source": [
    "from nltk.tokenize import word_tokenize\n",
    "from nltk.corpus import stopwords\n",
    "from nltk.stem import PorterStemmer, WordNetLemmatizer\n",
    "from collections import defaultdict"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 156,
   "id": "1dbbbbd7",
   "metadata": {},
   "outputs": [],
   "source": [
    "ps = PorterStemmer()\n",
    "lemmatizer = WordNetLemmatizer()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4fb3b5a7",
   "metadata": {},
   "source": [
    "# Read the documents"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 157,
   "id": "ba4760d2",
   "metadata": {},
   "outputs": [],
   "source": [
    "doc1 = \"Television is a wonderful scientific gift. It combines the advantages of cinema and radio. The most important and effective form of entertainment is television.\"\n",
    "doc2 = \"Everyone knows that paper is made from trees. But when one looks at trees, one cannot imagine that something so soft and fragile as the paper is made is so hard and strong. Plant materials such as wood are made of fibres known as cellulose.\"\n",
    "doc3 = \"Yesterday I saw a film titled Macbeth. Its story elements are interesting. The film’s hero, Macbeth, assassinates Duncan and ascends to the throne of Scotland.\""
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d9904308",
   "metadata": {},
   "source": [
    "# Merge all the documents"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 158,
   "id": "2c26f4bb",
   "metadata": {},
   "outputs": [],
   "source": [
    "docs = [doc1, doc2, doc3]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 159,
   "id": "85777a7e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Television is a wonderful scientific gift. It combines the advantages of cinema and radio. The most important and effective form of entertainment is television.', 'Everyone knows that paper is made from trees. But when one looks at trees, one cannot imagine that something so soft and fragile as the paper is made is so hard and strong. Plant materials such as wood are made of fibres known as cellulose.', 'Yesterday I saw a film titled Macbeth. Its story elements are interesting. The film’s hero, Macbeth, assassinates Duncan and ascends to the throne of Scotland.']\n"
     ]
    }
   ],
   "source": [
    "print(docs)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "76187edb",
   "metadata": {},
   "source": [
    "# 1) Tokenization"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 160,
   "id": "9977ec9d",
   "metadata": {},
   "outputs": [],
   "source": [
    "token1 = word_tokenize(doc1)\n",
    "token2 = word_tokenize(doc2)\n",
    "token3 = word_tokenize(doc3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 161,
   "id": "71991124",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Television', 'is', 'a', 'wonderful', 'scientific', 'gift', '.', 'It', 'combines', 'the', 'advantages', 'of', 'cinema', 'and', 'radio', '.', 'The', 'most', 'important', 'and', 'effective', 'form', 'of', 'entertainment', 'is', 'television', '.']\n"
     ]
    }
   ],
   "source": [
    "print(token1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 162,
   "id": "5f1f3904",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Everyone', 'knows', 'that', 'paper', 'is', 'made', 'from', 'trees', '.', 'But', 'when', 'one', 'looks', 'at', 'trees', ',', 'one', 'can', 'not', 'imagine', 'that', 'something', 'so', 'soft', 'and', 'fragile', 'as', 'the', 'paper', 'is', 'made', 'is', 'so', 'hard', 'and', 'strong', '.', 'Plant', 'materials', 'such', 'as', 'wood', 'are', 'made', 'of', 'fibres', 'known', 'as', 'cellulose', '.']\n"
     ]
    }
   ],
   "source": [
    "print(token2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 163,
   "id": "5540804f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Yesterday', 'I', 'saw', 'a', 'film', 'titled', 'Macbeth', '.', 'Its', 'story', 'elements', 'are', 'interesting', '.', 'The', 'film', '’', 's', 'hero', ',', 'Macbeth', ',', 'assassinates', 'Duncan', 'and', 'ascends', 'to', 'the', 'throne', 'of', 'Scotland', '.']\n"
     ]
    }
   ],
   "source": [
    "print(token3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 164,
   "id": "bc0c56cb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Television', 'is', 'a', 'wonderful', 'scientific', 'gift', '.', 'It', 'combines', 'the', 'advantages', 'of', 'cinema', 'and', 'radio', '.', 'The', 'most', 'important', 'and', 'effective', 'form', 'of', 'entertainment', 'is', 'television', '.', 'Everyone', 'knows', 'that', 'paper', 'is', 'made', 'from', 'trees', '.', 'But', 'when', 'one', 'looks', 'at', 'trees', ',', 'one', 'can', 'not', 'imagine', 'that', 'something', 'so', 'soft', 'and', 'fragile', 'as', 'the', 'paper', 'is', 'made', 'is', 'so', 'hard', 'and', 'strong', '.', 'Plant', 'materials', 'such', 'as', 'wood', 'are', 'made', 'of', 'fibres', 'known', 'as', 'cellulose', '.', 'Everyone', 'knows', 'that', 'paper', 'is', 'made', 'from', 'trees', '.', 'But', 'when', 'one', 'looks', 'at', 'trees', ',', 'one', 'can', 'not', 'imagine', 'that', 'something', 'so', 'soft', 'and', 'fragile', 'as', 'the', 'paper', 'is', 'made', 'is', 'so', 'hard', 'and', 'strong', '.', 'Plant', 'materials', 'such', 'as', 'wood', 'are', 'made', 'of', 'fibres', 'known', 'as', 'cellulose', '.']\n"
     ]
    }
   ],
   "source": [
    "term = token1+token2+token2\n",
    "print(term)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b7d3852f",
   "metadata": {},
   "source": [
    "# 2) LowerCase"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 165,
   "id": "157be292",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Doc 1 :\n",
      "['television', 'is', 'a', 'wonderful', 'scientific', 'gift', '.', 'it', 'combines', 'the', 'advantages', 'of', 'cinema', 'and', 'radio', '.', 'the', 'most', 'important', 'and', 'effective', 'form', 'of', 'entertainment', 'is', 'television', '.']\n",
      "Doc 2 :\n",
      "['everyone', 'knows', 'that', 'paper', 'is', 'made', 'from', 'trees', '.', 'but', 'when', 'one', 'looks', 'at', 'trees', ',', 'one', 'can', 'not', 'imagine', 'that', 'something', 'so', 'soft', 'and', 'fragile', 'as', 'the', 'paper', 'is', 'made', 'is', 'so', 'hard', 'and', 'strong', '.', 'plant', 'materials', 'such', 'as', 'wood', 'are', 'made', 'of', 'fibres', 'known', 'as', 'cellulose', '.']\n",
      "Doc 3 :\n",
      "['yesterday', 'i', 'saw', 'a', 'film', 'titled', 'macbeth', '.', 'its', 'story', 'elements', 'are', 'interesting', '.', 'the', 'film', '’', 's', 'hero', ',', 'macbeth', ',', 'assassinates', 'duncan', 'and', 'ascends', 'to', 'the', 'throne', 'of', 'scotland', '.']\n"
     ]
    }
   ],
   "source": [
    "LowerCaseone = []\n",
    "LowerCasetwo = []\n",
    "LowerCasethree = []\n",
    "for i in token1 :\n",
    "    LowerCaseone.append(i.lower())\n",
    "for i in token2 :\n",
    "    LowerCasetwo.append(i.lower())\n",
    "for i in token3 :\n",
    "    LowerCasethree.append(i.lower())\n",
    "\n",
    "print(\"Doc 1 :\")    \n",
    "print(LowerCaseone)\n",
    "print(\"Doc 2 :\")\n",
    "print(LowerCasetwo)\n",
    "print(\"Doc 3 :\")\n",
    "print(LowerCasethree)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "020e0d55",
   "metadata": {},
   "source": [
    "# 3) StopWords"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 166,
   "id": "fa21237e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Doc 1 :\n",
      "['television', 'wonderful', 'scientific', 'gift', '.', 'combines', 'advantages', 'cinema', 'radio', '.', 'important', 'effective', 'form', 'entertainment', 'television', '.']\n",
      "Doc 2 :\n",
      "['everyone', 'knows', 'paper', 'made', 'trees', '.', 'one', 'looks', 'trees', ',', 'one', 'imagine', 'something', 'soft', 'fragile', 'paper', 'made', 'hard', 'strong', '.', 'plant', 'materials', 'wood', 'made', 'fibres', 'known', 'cellulose', '.']\n",
      "Doc 3 :\n",
      "['yesterday', 'saw', 'film', 'titled', 'macbeth', '.', 'story', 'elements', 'interesting', '.', 'film', '’', 'hero', ',', 'macbeth', ',', 'assassinates', 'duncan', 'ascends', 'throne', 'scotland', '.']\n"
     ]
    }
   ],
   "source": [
    "Remove_stopWordsone = []\n",
    "Remove_stopWordstwo = []\n",
    "Remove_stopWordsthree = []\n",
    "for i in LowerCaseone:\n",
    "    if i not in stop_words:\n",
    "        Remove_stopWordsone.append(i)\n",
    "for i in LowerCasetwo:\n",
    "    if i not in stop_words:\n",
    "        Remove_stopWordstwo.append(i)\n",
    "for i in LowerCasethree:\n",
    "    if i not in stop_words:\n",
    "        Remove_stopWordsthree.append(i)\n",
    "\n",
    "print(\"Doc 1 :\")        \n",
    "print(Remove_stopWordsone)\n",
    "print(\"Doc 2 :\")\n",
    "print(Remove_stopWordstwo)\n",
    "print(\"Doc 3 :\")\n",
    "print(Remove_stopWordsthree)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b03d1963",
   "metadata": {},
   "source": [
    "# 4) Stemming"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 167,
   "id": "298fda59",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Doc 1 :\n",
      "['televis', 'wonder', 'scientif', 'gift', '.', 'combin', 'advantag', 'cinema', 'radio', '.', 'import', 'effect', 'form', 'entertain', 'televis', '.']\n",
      "Doc 2 :\n",
      "['everyon', 'know', 'paper', 'made', 'tree', '.', 'one', 'look', 'tree', ',', 'one', 'imagin', 'someth', 'soft', 'fragil', 'paper', 'made', 'hard', 'strong', '.', 'plant', 'materi', 'wood', 'made', 'fibr', 'known', 'cellulos', '.']\n",
      "Doc 3 :\n",
      "['yesterday', 'saw', 'film', 'titl', 'macbeth', '.', 'stori', 'element', 'interest', '.', 'film', '’', 'hero', ',', 'macbeth', ',', 'assassin', 'duncan', 'ascend', 'throne', 'scotland', '.']\n"
     ]
    }
   ],
   "source": [
    "Stemmingone = []\n",
    "Stemmingtwo = []\n",
    "Stemmingthree = []\n",
    "Stemmingfour = []\n",
    "for x in Remove_stopWordsone:\n",
    "    Stemmingone.append(ps.stem(x))\n",
    "for y in Remove_stopWordstwo:\n",
    "    Stemmingtwo.append(ps.stem(y))\n",
    "for z in Remove_stopWordsthree:\n",
    "    Stemmingthree.append(ps.stem(z))\n",
    "\n",
    "print(\"Doc 1 :\")\n",
    "print(Stemmingone)\n",
    "print(\"Doc 2 :\")\n",
    "print(Stemmingtwo)\n",
    "print(\"Doc 3 :\")\n",
    "print(Stemmingthree)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f06ea501",
   "metadata": {},
   "source": [
    "# Final Merge for all terms"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 168,
   "id": "27058267",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['televis', 'wonder', 'scientif', 'gift', '.', 'combin', 'advantag', 'cinema', 'radio', '.', 'import', 'effect', 'form', 'entertain', 'televis', '.', 'everyon', 'know', 'paper', 'made', 'tree', '.', 'one', 'look', 'tree', ',', 'one', 'imagin', 'someth', 'soft', 'fragil', 'paper', 'made', 'hard', 'strong', '.', 'plant', 'materi', 'wood', 'made', 'fibr', 'known', 'cellulos', '.', 'yesterday', 'saw', 'film', 'titl', 'macbeth', '.', 'stori', 'element', 'interest', '.', 'film', '’', 'hero', ',', 'macbeth', ',', 'assassin', 'duncan', 'ascend', 'throne', 'scotland', '.']\n"
     ]
    }
   ],
   "source": [
    "final_term = Stemmingone+Stemmingtwo+Stemmingthree\n",
    "print(final_term)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3f80763e",
   "metadata": {},
   "source": [
    "# 5) Removal of special characters, numbers, and punctuations if needed "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 169,
   "id": "fd6bd3c3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['televis', 'wonder', 'scientif', 'gift', '', 'combin', 'advantag', 'cinema', 'radio', '', 'import', 'effect', 'form', 'entertain', 'televis', '', 'everyon', 'know', 'paper', 'made', 'tree', '', 'one', 'look', 'tree', '', 'one', 'imagin', 'someth', 'soft', 'fragil', 'paper', 'made', 'hard', 'strong', '', 'plant', 'materi', 'wood', 'made', 'fibr', 'known', 'cellulos', '', 'yesterday', 'saw', 'film', 'titl', 'macbeth', '', 'stori', 'element', 'interest', '', 'film', '', 'hero', '', 'macbeth', '', 'assassin', 'duncan', 'ascend', 'throne', 'scotland', '']\n"
     ]
    }
   ],
   "source": [
    "for x in final_term:\n",
    "    words = [re.sub(r'[^a-zA-Z0-9]+', '', word) for word in final_term]\n",
    "    \n",
    "\n",
    "print(words)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a194a42e",
   "metadata": {},
   "source": [
    "# 6) Remove duplicates"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 177,
   "id": "ac2ce54f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['', 'look', 'know', 'tree', 'strong', 'wood', 'film', 'ascend', 'soft', 'scotland', 'cellulos', 'scientif', 'import', 'imagin', 'plant', 'everyon', 'titl', 'hard', 'one', 'gift', 'paper', 'materi', 'entertain', 'yesterday', 'televis', 'combin', 'hero', 'wonder', 'known', 'macbeth', 'throne', 'someth', 'assassin', 'form', 'cinema', 'element', 'stori', 'fibr', 'advantag', 'effect', 'made', 'fragil', 'saw', 'radio', 'interest', 'duncan']\n"
     ]
    }
   ],
   "source": [
    "for x in words:\n",
    "   final_process = list(set(words))\n",
    "print(final_process)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 184,
   "id": "3fbff999",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['look', 'know', 'tree', 'strong', 'wood', 'film', 'ascend', 'soft', 'scotland', 'cellulos', 'scientif', 'import', 'imagin', 'plant', 'everyon', 'titl', 'hard', 'one', 'gift', 'paper', 'materi', 'entertain', 'yesterday', 'televis', 'combin', 'hero', 'wonder', 'known', 'macbeth', 'throne', 'someth', 'assassin', 'form', 'cinema', 'element', 'stori', 'fibr', 'advantag', 'effect', 'made', 'fragil', 'saw', 'radio', 'interest', 'duncan']\n"
     ]
    }
   ],
   "source": [
    "final_processtwo = []\n",
    "for x in final_process:\n",
    "    if x!= '':\n",
    "        final_processtwo.append(x)\n",
    "\n",
    "print(final_processtwo)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "71999db7",
   "metadata": {},
   "source": [
    "# Sorting"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 190,
   "id": "6b3c8291",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['advantag', 'ascend', 'assassin', 'cellulos', 'cinema', 'combin', 'duncan', 'effect', 'element', 'entertain', 'everyon', 'fibr', 'film', 'form', 'fragil', 'gift', 'hard', 'hero', 'imagin', 'import', 'interest', 'know', 'known', 'look', 'macbeth', 'made', 'materi', 'one', 'paper', 'plant', 'radio', 'saw', 'scientif', 'scotland', 'soft', 'someth', 'stori', 'strong', 'televis', 'throne', 'titl', 'tree', 'wonder', 'wood', 'yesterday']\n"
     ]
    }
   ],
   "source": [
    "final_processtwo = sorted(final_processtwo)\n",
    "\n",
    "print(final_processtwo)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "75469d44",
   "metadata": {},
   "source": [
    "# Construct the TDIM"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 191,
   "id": "0322dc45",
   "metadata": {},
   "outputs": [],
   "source": [
    "tdim = [[] for i in range(len(final_processtwo))]\n",
    "for i in range(len(final_processtwo)):\n",
    "    tdim[i].append(final_processtwo[i])\n",
    "    if final_processtwo[i] in Stemmingone:\n",
    "        tdim[i].append(1)\n",
    "    else: \n",
    "        tdim[i].append(0)\n",
    "    if final_processtwo[i] in Stemmingtwo:\n",
    "        tdim[i].append(1)\n",
    "    else: \n",
    "        tdim[i].append(0)\n",
    "    if final_processtwo[i] in Stemmingthree:\n",
    "        tdim[i].append(1)\n",
    "    else: \n",
    "        tdim[i].append(0)\n",
    "    "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3e3537c6",
   "metadata": {},
   "source": [
    "# Final Output"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 192,
   "id": "d2c7e093",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " word, Doc1, Doc2, Doc3\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "[['advantag', 1, 0, 0],\n",
       " ['ascend', 0, 0, 1],\n",
       " ['assassin', 0, 0, 1],\n",
       " ['cellulos', 0, 1, 0],\n",
       " ['cinema', 1, 0, 0],\n",
       " ['combin', 1, 0, 0],\n",
       " ['duncan', 0, 0, 1],\n",
       " ['effect', 1, 0, 0],\n",
       " ['element', 0, 0, 1],\n",
       " ['entertain', 1, 0, 0],\n",
       " ['everyon', 0, 1, 0],\n",
       " ['fibr', 0, 1, 0],\n",
       " ['film', 0, 0, 1],\n",
       " ['form', 1, 0, 0],\n",
       " ['fragil', 0, 1, 0],\n",
       " ['gift', 1, 0, 0],\n",
       " ['hard', 0, 1, 0],\n",
       " ['hero', 0, 0, 1],\n",
       " ['imagin', 0, 1, 0],\n",
       " ['import', 1, 0, 0],\n",
       " ['interest', 0, 0, 1],\n",
       " ['know', 0, 1, 0],\n",
       " ['known', 0, 1, 0],\n",
       " ['look', 0, 1, 0],\n",
       " ['macbeth', 0, 0, 1],\n",
       " ['made', 0, 1, 0],\n",
       " ['materi', 0, 1, 0],\n",
       " ['one', 0, 1, 0],\n",
       " ['paper', 0, 1, 0],\n",
       " ['plant', 0, 1, 0],\n",
       " ['radio', 1, 0, 0],\n",
       " ['saw', 0, 0, 1],\n",
       " ['scientif', 1, 0, 0],\n",
       " ['scotland', 0, 0, 1],\n",
       " ['soft', 0, 1, 0],\n",
       " ['someth', 0, 1, 0],\n",
       " ['stori', 0, 0, 1],\n",
       " ['strong', 0, 1, 0],\n",
       " ['televis', 1, 0, 0],\n",
       " ['throne', 0, 0, 1],\n",
       " ['titl', 0, 0, 1],\n",
       " ['tree', 0, 1, 0],\n",
       " ['wonder', 1, 0, 0],\n",
       " ['wood', 0, 1, 0],\n",
       " ['yesterday', 0, 0, 1]]"
      ]
     },
     "execution_count": 192,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "print(\" word, Doc1, Doc2, Doc3\")\n",
    "tdim"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f27c0e09",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
