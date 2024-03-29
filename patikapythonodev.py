# -*- coding: utf-8 -*-
"""PatikaPythonOdev.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Md4unA8rTM0d_4vZvBD1_Ua_tD7783_h
"""

import ast

def flatten_list(lst):
    flattened_list = []
    for item in lst:
        if isinstance(item, list):
            flattened_list.extend(flatten_list(item))
        else:
            flattened_list.append(item)
    return flattened_list

def reverse_list(lst):
    reversed_list = []
    for item in lst[::-1]:
        if isinstance(item, list):
            reversed_list.append(reverse_list(item))
        else:
            reversed_list.append(item)
    return reversed_list

print("Lütfen bir liste girin (örn. [[1, 2], [3, 4], [5, 6, 7]]), çıkmak için 'exit' yazın.")

while True:
    input_list_str = input("Liste: ")
    if input_list_str.lower() == 'exit':
        print("Programdan çıkıldı.")
        break
    try:
        input_list = ast.literal_eval(input_list_str)
        print("Yapılacak işlemi seçin: 'flatten' veya 'reverse'.")
        choice = input("İşlem: ").strip().lower()
        if choice == "flatten":
            output = flatten_list(input_list)
            print("Düzleştirilmiş liste:", output)
        elif choice == "reverse":
            output = reverse_list(input_list)
            print("Tersine döndürülmüş liste:", output)
        else:
            print("Geçersiz işlem seçimi. Liste girin ve 'flatten' veya 'reverse' seçin.") #Buraya bir daha bak. Tekrar liste istiyor. İşlemi tekrar istemeli
    except SyntaxError:
        print("Geçersiz giriş. Lütfen doğru bir liste formatı girin.")
    except ValueError:
        print("Geçersiz giriş. Lütfen doğru bir liste formatı girin.")