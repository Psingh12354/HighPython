{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "7a2b8697",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0    H\n",
      "1    I\n",
      "2    G\n",
      "3    H\n",
      "dtype: object\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "data=np.array(['H','I','G','H'])\n",
    "series=pd.Series(data)\n",
    "print(series)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e5e71003",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c2b8704b",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "5f31143a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'H'"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "series[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "44e1bd72",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Name</th>\n",
       "      <th>Universe</th>\n",
       "      <th>Powers</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Batman</td>\n",
       "      <td>DC</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Wolverine</td>\n",
       "      <td>Marvel</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Naruto</td>\n",
       "      <td>Anime</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Jedi</td>\n",
       "      <td>StarWars</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        Name  Universe  Powers\n",
       "0     Batman        DC       3\n",
       "1  Wolverine    Marvel       3\n",
       "2     Naruto     Anime       4\n",
       "3       Jedi  StarWars       5"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pd.DataFrame()\n",
    "names = ['Batman','Wolverine','Naruto','Jedi']\n",
    "universe = ['DC','Marvel','Anime','StarWars']\n",
    "powers = [3,3,4,5]\n",
    "\n",
    "df['Name'] = names\n",
    "df['Universe'] = universe\n",
    "df['Powers'] = powers\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "081a6ab0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Names</th>\n",
       "      <th>Universe</th>\n",
       "      <th>Power</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Batman</td>\n",
       "      <td>DC</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Wolverine</td>\n",
       "      <td>Marvel</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Naruto</td>\n",
       "      <td>Anime</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Jedi</td>\n",
       "      <td>StarWars</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       Names  Universe  Power\n",
       "0     Batman        DC      3\n",
       "1  Wolverine    Marvel      3\n",
       "2     Naruto     Anime      4\n",
       "3       Jedi  StarWars      5"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Rename column name\n",
    "df.rename(columns={'Name':'Names','Powers':'Power'},inplace=True)\n",
    "df.head()\n",
    "#Rename other approach is just overwrite"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "57a6ad51",
   "metadata": {},
   "outputs": [],
   "source": [
    "# axix=1 means action perform on col\n",
    "df.drop('Power', axis=1, inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "55756fef",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Names</th>\n",
       "      <th>Universe</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Batman</td>\n",
       "      <td>DC</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Wolverine</td>\n",
       "      <td>Marvel</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Naruto</td>\n",
       "      <td>Anime</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Jedi</td>\n",
       "      <td>StarWars</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       Names  Universe\n",
       "0     Batman        DC\n",
       "1  Wolverine    Marvel\n",
       "2     Naruto     Anime\n",
       "3       Jedi  StarWars"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "6c08c512",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-43-1f175a603ec5>, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-43-1f175a603ec5>\"\u001b[1;36m, line \u001b[1;32m1\u001b[0m\n\u001b[1;33m    df.drop([0:1],axis=0,inplace=True)\u001b[0m\n\u001b[1;37m              ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "df.drop([0,1],axis=0,inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "e6066452",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Names</th>\n",
       "      <th>Universe</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Naruto</td>\n",
       "      <td>Anime</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Jedi</td>\n",
       "      <td>StarWars</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    Names  Universe\n",
       "2  Naruto     Anime\n",
       "3    Jedi  StarWars"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "017627ef",
   "metadata": {},
   "outputs": [],
   "source": [
    "#sorting\n",
    "#movies->dataframe name\n",
    "#movies.title here title is column name\n",
    "#movies.title.sort_values() #sorting according to the vlaues\n",
    "#Example"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "21bfd1d9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3      Jedi\n",
       "2    Naruto\n",
       "Name: Names, dtype: object"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.Names.sort_values()\n",
    "#or"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "11c38bad",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Names</th>\n",
       "      <th>Universe</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Jedi</td>\n",
       "      <td>StarWars</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Naruto</td>\n",
       "      <td>Anime</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    Names  Universe\n",
       "3    Jedi  StarWars\n",
       "2  Naruto     Anime"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.sort_values('Names')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "7c38526c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Name</th>\n",
       "      <th>Universe</th>\n",
       "      <th>Powers</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Batman</td>\n",
       "      <td>DC</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Wolverine</td>\n",
       "      <td>Marvel</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Naruto</td>\n",
       "      <td>Anime</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Jedi</td>\n",
       "      <td>StarWars</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        Name  Universe  Powers\n",
       "0     Batman        DC       3\n",
       "1  Wolverine    Marvel       3\n",
       "2     Naruto     Anime       4\n",
       "3       Jedi  StarWars       5"
      ]
     },
     "execution_count": 49,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pd.DataFrame()\n",
    "names = ['Batman','Wolverine','Naruto','Jedi']\n",
    "universe = ['DC','Marvel','Anime','StarWars']\n",
    "powers = [3,3,4,5]\n",
    "\n",
    "df['Name'] = names\n",
    "df['Universe'] = universe\n",
    "df['Powers'] = powers\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "0193b42d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Name</th>\n",
       "      <th>Universe</th>\n",
       "      <th>Powers</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Naruto</td>\n",
       "      <td>Anime</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Jedi</td>\n",
       "      <td>StarWars</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     Name  Universe  Powers\n",
       "2  Naruto     Anime       4\n",
       "3    Jedi  StarWars       5"
      ]
     },
     "execution_count": 50,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#to apply condition use filter\n",
    "df[df.Powers>3]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "bcbc1ccf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Name</th>\n",
       "      <th>Universe</th>\n",
       "      <th>Powers</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Batman</td>\n",
       "      <td>DC</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Wolverine</td>\n",
       "      <td>Marvel</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Naruto</td>\n",
       "      <td>Anime</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        Name Universe  Powers\n",
       "0     Batman       DC       3\n",
       "1  Wolverine   Marvel       3\n",
       "2     Naruto    Anime       4"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.loc[0:2,:]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "f9e585f2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Name</th>\n",
       "      <th>Powers</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Batman</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Wolverine</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Naruto</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        Name  Powers\n",
       "0     Batman       3\n",
       "1  Wolverine       3\n",
       "2     Naruto       4"
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.loc[0:2,['Name','Powers']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "4d141ac9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Name</th>\n",
       "      <th>Universe</th>\n",
       "      <th>Powers</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Batman</td>\n",
       "      <td>DC</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     Name Universe  Powers\n",
       "0  Batman       DC       3"
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.loc[df.Name==\"Batman\",:]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "875d39c5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Name</th>\n",
       "      <th>Universe</th>\n",
       "      <th>Powers</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Batman</td>\n",
       "      <td>DC</td>\n",
       "      <td>3.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Wolverine</td>\n",
       "      <td>Marvel</td>\n",
       "      <td>3.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Naruto</td>\n",
       "      <td>Anime</td>\n",
       "      <td>4.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Jedi</td>\n",
       "      <td>StarWars</td>\n",
       "      <td>5.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        Name  Universe  Powers\n",
       "0     Batman        DC     3.0\n",
       "1  Wolverine    Marvel     3.0\n",
       "2     Naruto     Anime     4.0\n",
       "3       Jedi  StarWars     5.0"
      ]
     },
     "execution_count": 64,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#change datatype\n",
    "df.dtypes\n",
    "df['Powers']=df.Powers.astype(float)\n",
    "df\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "id": "e0cc883c",
   "metadata": {},
   "outputs": [
    {
     "ename": "KeyError",
     "evalue": "\"None of ['Name'] are in the columns\"",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mKeyError\u001b[0m                                  Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-79-2abe5f177682>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;31m#Make any Column your index value\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[0mdf\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mset_index\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'Name'\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0minplace\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mTrue\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      3\u001b[0m \u001b[0mdf\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mindex\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32me:\\internship\\venv\\lib\\site-packages\\pandas\\core\\frame.py\u001b[0m in \u001b[0;36mset_index\u001b[1;34m(self, keys, drop, append, inplace, verify_integrity)\u001b[0m\n\u001b[0;32m   4725\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   4726\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[0mmissing\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 4727\u001b[1;33m             \u001b[1;32mraise\u001b[0m \u001b[0mKeyError\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34mf\"None of {missing} are in the columns\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   4728\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   4729\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[0minplace\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mKeyError\u001b[0m: \"None of ['Name'] are in the columns\""
     ]
    }
   ],
   "source": [
    "#Make any Column your index value\n",
    "df.set_index('Name',inplace=True)\n",
    "df.index"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "67884ae0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['Batman', 'Wolverine', 'Naruto', 'Jedi'], dtype='object', name='Name')"
      ]
     },
     "execution_count": 71,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d0184006",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Dummy Variable also known as indicator values\n",
    "#Example gender col male 1 and female 0\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "id": "ce780a41",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'hello' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-81-21e6f2dead05>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[1;31m#Method called pickling\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[1;31m#In csv a col contain string might be considered as int\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 4\u001b[1;33m \u001b[0mdf\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mto_pickle\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mhello\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mtxt\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      5\u001b[0m \u001b[0mdf\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mread_pickle\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mhello\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mtxt\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'hello' is not defined"
     ]
    }
   ],
   "source": [
    "#pickle is use for serialization or de-serialozaton\n",
    "#Method called pickling\n",
    "#In csv a col contain string might be considered as int\n",
    "df.to_pickle(hello)\n",
    "df.read_pickle(hello)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "id": "59f0b15c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3   Universe  Powers\n",
      "0       DC       3\n",
      "1   Marvel       3\n",
      "4   Universe  Powers\n",
      "2    Anime       4\n",
      "5    Universe  Powers\n",
      "3  StarWars       5\n"
     ]
    }
   ],
   "source": [
    "#groupby is use to split the table data into groups\n",
    "grouped=df.groupby('Powers')\n",
    "for x,y in grouped:\n",
    "    print(x, y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "id": "c212d2de",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-89-6247afef3651>, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-89-6247afef3651>\"\u001b[1;36m, line \u001b[1;32m1\u001b[0m\n\u001b[1;33m    df.groupby'Powers'.agg(['mean','min','max','sum','count'])\u001b[0m\n\u001b[1;37m              ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "df.groupby'Powers'.agg(['mean','min','max','sum','count'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "3789b072",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Name</th>\n",
       "      <th>Universe</th>\n",
       "      <th>Powers</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Batman</td>\n",
       "      <td>DC</td>\n",
       "      <td>3.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Wolverine</td>\n",
       "      <td>Marvel</td>\n",
       "      <td>3.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Naruto</td>\n",
       "      <td>Anime</td>\n",
       "      <td>4.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Jedi</td>\n",
       "      <td>StarWars</td>\n",
       "      <td>5.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        Name  Universe  Powers\n",
       "0     Batman        DC     3.0\n",
       "1  Wolverine    Marvel     3.0\n",
       "2     Naruto     Anime     4.0\n",
       "3       Jedi  StarWars     5.0"
      ]
     },
     "execution_count": 63,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "51cfee75",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Name</th>\n",
       "      <th>Universe</th>\n",
       "      <th>Powers</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Batman</td>\n",
       "      <td>DC</td>\n",
       "      <td>3.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Wolverine</td>\n",
       "      <td>Marvel</td>\n",
       "      <td>3.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Naruto</td>\n",
       "      <td>Anime</td>\n",
       "      <td>4.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Jedi</td>\n",
       "      <td>StarWars</td>\n",
       "      <td>5.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        Name  Universe  Powers\n",
       "0     Batman        DC     3.0\n",
       "1  Wolverine    Marvel     3.0\n",
       "2     Naruto     Anime     4.0\n",
       "3       Jedi  StarWars     5.0"
      ]
     },
     "execution_count": 62,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": []
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
