#!/usr/bin/env python
# coding: utf-8

# In[1]:


def is_palindrome(word):
    if word[::-1] == word:
        print(word + ' is a palindrome.')
    else:
        print(word + ' is not a palindrome')
        


# In[2]:


word = input('Enter a word:\n')
is_palindrome(word)

