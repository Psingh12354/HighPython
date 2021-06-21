{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "e06f8c9b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'e_id': 1111, 'e_name': 'Priyanshu', 'dob': '16082000'}\n"
     ]
    }
   ],
   "source": [
    "emp={'e_id': 1111,'e_name':'Priyanshu','dob':'16082000'}\n",
    "print(emp)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "3f8205cb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "e_id\n",
      "e_name\n",
      "dob\n"
     ]
    }
   ],
   "source": [
    "for x in emp:\n",
    "    print(x)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "8c6a5b2a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "dict_values([1111, 'Priyanshu', '16082000'])\n"
     ]
    }
   ],
   "source": [
    "print(emp.values())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "877f38c7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "e_id\n",
      "e_name\n",
      "dob\n"
     ]
    }
   ],
   "source": [
    "for x in emp.keys():\n",
    "    print(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "0cef9c9d",
   "metadata": {},
   "outputs": [],
   "source": [
    "emp['bg']='B+'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "e819f0ff",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'e_id': 1111, 'e_name': 'Priyanshu', 'dob': '16082000', 'bg': 'B+'}\n"
     ]
    }
   ],
   "source": [
    "print(emp)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "b98bc3b4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "e_id\n",
      "e_name\n",
      "dob\n"
     ]
    }
   ],
   "source": [
    "for x,y in emp.items():\n",
    "    print(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "954ea4bb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Priyanshu'"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "emp.pop('e_name')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "61e293b8",
   "metadata": {},
   "outputs": [],
   "source": [
    "string=\"Hello World\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "28a14218",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Hello World'"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "string"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "dfacdfe5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "string.startswith('H')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "9ef42e88",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Hello WorldHello WorldHello WorldHello WorldHello WorldHello WorldHello WorldHello WorldHello WorldHello World'"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "string*10\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "edb02caa",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'dlroW olleH'"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "string[::-1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "ef8d6bd8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'hello World'"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "string.replace(\"Hello\",\"hello\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "e8cec211",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{10, 20}\n"
     ]
    }
   ],
   "source": [
    "myset=set([10,20,20])\n",
    "print(myset)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "b8da9f0c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5"
      ]
     },
     "execution_count": 55,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "file.write(\"HEllo\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "4666bab6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'HEllo'"
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "file.read()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "625d71a3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "division by zero\n"
     ]
    }
   ],
   "source": [
    "a=1\n",
    "b=0\n",
    "try:\n",
    "    c=a/b\n",
    "except Exception as e:\n",
    "    print(e)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
