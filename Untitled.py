#!/usr/bin/env python
# coding: utf-8

# In[1]:


def get_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = get_even_numbers(numbers)
print(even_numbers)


# In[ ]:




