# Soma elementos de uma lista (for e return)
def sum_list(lst):
    total = 0
    for x in lst:
        total += x
    return total

# Produto de elementos em uma lista (for e return)
def product_list(lst):
    result = 1
    for x in lst:
        result *= x
    return result

# Encontra o valor máximo em uma lista (for, if/else)
def max_in_list(lst):
    if not lst:
        return None
    max_val = lst[0]
    for x in lst:
        if x > max_val:
            max_val = x
    return max_val

# Encontra o valor mínimo em uma lista (for, if/else)
def min_in_list(lst):
    if not lst:
        return None
    min_val = lst[0]
    for x in lst:
        if x < min_val:
            min_val = x
    return min_val

# Calcula a média de uma lista (for, if/else)
def average(lst):
    if not lst:
        return None
    total = 0
    for x in lst:
        total += x
    return total / len(lst)

# Calcula o fatorial de um número (for)
def factorial(n):
    if n < 0:
        return None
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Inverte uma lista (for)
def reverse_list(lst):
    result = []
    for i in range(len(lst)-1, -1, -1):
        result.append(lst[i])
    return result

# Verifica se um elemento está em uma lista (for e break)
def contains(lst, value):
    for item in lst:
        if item == value:
            return True
    return False

# Encontra índice de um elemento em uma lista (for, if)
def find_index(lst, value):
    for i, item in enumerate(lst):
        if item == value:
            return i
    return -1

# Mescla duas listas ordenadas (while, if/else)
def merge_sorted(a, b):
    i = j = 0
    result = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result

# Busca binária em lista ordenada (while, if/else)
def binary_search(lst, target):
    low, high = 0, len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return None

# Ordenação bubble sort (for, if/else, break)
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True
        if not swapped:
            break
    return lst

# Classifica temperatura em texto (if/elif)
def temperature_status(c):
    if c <= 0:
        return 'congelante'
    elif c < 20:
        return 'frio'
    elif c < 30:
        return 'agradável'
    else:
        return 'quente'

# Dias de um mês dado (match)
def days_in_month(month, leap=False):
    match month:
        case 2:
            return 29 if leap else 28
        case 4 | 6 | 9 | 11:
            return 30
        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
            return 31
        case _:
            return None

# Classifica idade (if/elif)
def classify_age(age):
    if age < 0:
        return 'inválido'
    elif age < 18:
        return 'menor'
    elif age < 65:
        return 'adulto'
    else:
        return 'idoso'

# Par ou ímpar (if/else)
def parity(n):
    if n % 2 == 0:
        return 'par'
    else:
        return 'ímpar'

# Máximo divisor comum (gcd) (if, while)
def gcd(a, b):
    if b == 0:
        return a
    while b:
        a, b = b, a % b
    return a

# Mínimo múltiplo comum (lcm) (if, if, return)
def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    if a < b:
        a, b = b, a
    return abs(a * b) // gcd(a, b)

# Converte para binário (while, if)
def to_binary(n):
    if n == 0:
        return '0'
    bits = []
    while n > 0:
        bits.append(str(n % 2))
        n //= 2
    bits.reverse()
    return ''.join(bits)

# Converte para hexadecimal (while, if)
def to_hex(n):
    if n == 0:
        return '0'
    chars = '0123456789ABCDEF'
    result = []
    while n > 0:
        result.append(chars[n % 16])
        n //= 16
    return ''.join(reversed(result))

# Achata lista de listas (for)
def flatten(lst):
    result = []
    for sub in lst:
        for item in sub:
            result.append(item)
    return result

# Encontra a palavra mais longa (for, if)
def find_longest_word(words):
    if not words:
        return None
    longest = words[0]
    for w in words[1:]:
        if len(w) > len(longest):
            longest = w
    return longest

# Converte string para título (for)
def title_case(s):
    words = s.split()
    result = []
    for w in words:
        result.append(w.capitalize())
    return ' '.join(result)

# Filtra palíndromos em lista (for, if)
def palindrome_list(lst):
    result = []
    for x in lst:
        s = str(x)
        if s == s[::-1]:
            result.append(x)
    return result

# Conta palavras em string (if)
def count_words(s):
    s = s.strip()
    if not s:
        return 0
    return len(s.split())

# Filtra números pares em lista (for, if)
def filter_even(lst):
    result = []
    for x in lst:
        if x % 2 == 0:
            result.append(x)
    return result

# Filtra números ímpares em lista (for, if)
def filter_odd(lst):
    result = []
    for x in lst:
        if x % 2 != 0:
            result.append(x)
    return result

# Remove duplicados mantendo ordem (for, if)
def distinct(lst):
    result = []
    for x in lst:
        if x not in result:
            result.append(x)
    return result

# Soma valores em índices pares (for, if)
def sum_even_index(lst):
    total = 0
    for i, x in enumerate(lst):
        if i % 2 == 0:
            total += x
    return total

# Soma valores em índices ímpares (for, if)
def sum_odd_index(lst):
    total = 0
    for i, x in enumerate(lst):
        if i % 2 != 0:
            total += x
    return total

# Nome do mês (match)
def month_name(n):
    match n:
        case 1: return 'Janeiro'
        case 2: return 'Fevereiro'
        case 3: return 'Março'
        case 4: return 'Abril'
        case 5: return 'Maio'
        case 6: return 'Junho'
        case 7: return 'Julho'
        case 8: return 'Agosto'
        case 9: return 'Setembro'
        case 10: return 'Outubro'
        case 11: return 'Novembro'
        case 12: return 'Dezembro'
        case _: return 'Inválido'

# Verifica ano bissexto (if/elif)
def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

# Cifra de César (encrypt) (for, if)
def encrypt_caesar(s, shift):
    result = ''
    for c in s:
        if 'a' <= c <= 'z':
            result += chr((ord(c) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += c
    return result

# Cifra de César (decrypt) (for, if/elif)
def decrypt_caesar(s, shift):
    result = ''
    for c in s:
        if 'A' <= c <= 'Z':
            result += chr((ord(c) - ord('A') - shift) % 26 + ord('A'))
        elif 'a' <= c <= 'z':
            result += chr((ord(c) - ord('a') - shift) % 26 + ord('a'))
        else:
            result += c
    return result

# Verifica anagrama (if, sort)
def is_anagram(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)

# Conta ocorrências de um caractere (for, if)
def count_char(s, char):
    count = 0
    for c in s:
        if c == char:
            count += 1
    return count

# Substitui caractere em string (for, if/else)
def replace_char(s, old, new):
    result = ''
    for c in s:
        if c == old:
            result += new
        else:
            result += c
    return result

# Soma dígitos de um número (for)
def sum_digits(n):
    total = 0
    for d in str(abs(n)):
        total += int(d)
    return total

# Conta dígitos de um número (if, for)
def digit_count(n):
    if n == 0:
        return 1
    count = 0
    for _ in str(abs(n)):
        count += 1
    return count

# Divisão segura (if)
def safe_divide(a, b):
    if b == 0:
        return None
    result = a / b
    return result

# Encontra o primeiro caractere maiúsculo em uma string (for, if)
def find_first_upper(s):
    for char in s:
        if char.isupper():
            return char
    return None 