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


# ============================================
# FUNÇÕES COMPLEXAS - Recursão
# ============================================

# Fibonacci recursivo (recursão, if/elif)
def fibonacci(n):
    if n < 0:
        return None
    elif n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Soma recursiva de lista (recursão, if)
def recursive_sum(lst):
    if not lst:
        return 0
    return lst[0] + recursive_sum(lst[1:])


# Potência recursiva (recursão, if/elif)
def power(base, exp):
    if exp < 0:
        return None
    elif exp == 0:
        return 1
    elif exp == 1:
        return base
    else:
        return base * power(base, exp - 1)


# Contagem regressiva recursiva (recursão, if)
def countdown(n):
    if n <= 0:
        return [0]
    return [n] + countdown(n - 1)


# ============================================
# FUNÇÕES COMPLEXAS - Try/Except
# ============================================

# Parser de inteiro seguro (try/except)
def safe_int(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        return None


# Parser de float seguro (try/except)
def safe_float(value):
    try:
        return float(value)
    except (ValueError, TypeError):
        return None


# Acesso seguro a dicionário (try/except, if)
def safe_get(d, key, default=None):
    try:
        if not isinstance(d, dict):
            return default
        return d.get(key, default)
    except Exception:
        return default


# Divisão com tratamento de exceção (try/except)
def divide_safe(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None
    except TypeError:
        return None


# ============================================
# FUNÇÕES COMPLEXAS - Múltiplas Condições
# ============================================

# Validador de senha (múltiplos if)
def validate_password(password):
    if len(password) < 8:
        return 'muito_curta'
    
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in '!@#$%^&*()_+-=':
            has_special = True
    
    if not has_upper:
        return 'sem_maiuscula'
    if not has_lower:
        return 'sem_minuscula'
    if not has_digit:
        return 'sem_numero'
    if not has_special:
        return 'sem_especial'
    
    return 'valida'


# Calculadora de desconto (múltiplos if/elif)
def calculate_discount(price, customer_type, quantity):
    if price <= 0 or quantity <= 0:
        return 0
    
    discount = 0
    
    # Desconto por tipo de cliente
    if customer_type == 'vip':
        discount += 0.20
    elif customer_type == 'premium':
        discount += 0.10
    elif customer_type == 'regular':
        discount += 0.05
    
    # Desconto por quantidade
    if quantity >= 100:
        discount += 0.15
    elif quantity >= 50:
        discount += 0.10
    elif quantity >= 10:
        discount += 0.05
    
    # Limita desconto máximo
    if discount > 0.30:
        discount = 0.30
    
    return round(price * quantity * (1 - discount), 2)


# Classificador de triângulo (múltiplos if)
def classify_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 'invalido'
    
    if a + b <= c or b + c <= a or a + c <= b:
        return 'invalido'
    
    if a == b == c:
        return 'equilatero'
    elif a == b or b == c or a == c:
        return 'isosceles'
    else:
        return 'escaleno'


# Calculadora de IMC com classificação (múltiplos if/elif)
def calculate_bmi(weight, height):
    if weight <= 0 or height <= 0:
        return None, 'invalido'
    
    bmi = weight / (height ** 2)
    bmi = round(bmi, 2)
    
    if bmi < 18.5:
        return bmi, 'abaixo_peso'
    elif bmi < 25:
        return bmi, 'normal'
    elif bmi < 30:
        return bmi, 'sobrepeso'
    elif bmi < 35:
        return bmi, 'obesidade_1'
    elif bmi < 40:
        return bmi, 'obesidade_2'
    else:
        return bmi, 'obesidade_3'


# ============================================
# FUNÇÕES COMPLEXAS - Estruturas Aninhadas
# ============================================

# Busca em dicionário aninhado (recursão, if)
def deep_get(d, keys, default=None):
    if not keys:
        return d
    if not isinstance(d, dict):
        return default
    
    key = keys[0]
    if key not in d:
        return default
    
    return deep_get(d[key], keys[1:], default)


# Achata dicionário aninhado (recursão, if/else)
def flatten_dict(d, parent_key='', sep='.'):
    items = {}
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.update(flatten_dict(v, new_key, sep))
        else:
            items[new_key] = v
    return items


# Conta profundidade de lista aninhada (recursão, if)
def list_depth(lst):
    if not isinstance(lst, list):
        return 0
    if not lst:
        return 1
    return 1 + max(list_depth(item) for item in lst)


# ============================================
# FUNÇÕES COMPLEXAS - Validação
# ============================================

# Validador de email simplificado (múltiplos if)
def validate_email(email):
    if not email or not isinstance(email, str):
        return False
    
    if email.count('@') != 1:
        return False
    
    local, domain = email.split('@')
    
    if not local or not domain:
        return False
    
    if '.' not in domain:
        return False
    
    if domain.startswith('.') or domain.endswith('.'):
        return False
    
    if '..' in email:
        return False
    
    return True


# Validador de CPF (múltiplos if, for)
def validate_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))
    
    if len(cpf) != 11:
        return False
    
    if cpf == cpf[0] * 11:
        return False
    
    # Primeiro dígito verificador
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    resto = soma % 11
    digito1 = 0 if resto < 2 else 11 - resto
    
    if int(cpf[9]) != digito1:
        return False
    
    # Segundo dígito verificador
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    resto = soma % 11
    digito2 = 0 if resto < 2 else 11 - resto
    
    if int(cpf[10]) != digito2:
        return False
    
    return True


# ============================================
# FUNÇÕES COMPLEXAS - Algoritmos
# ============================================

# Quicksort (recursão, if, for)
def quicksort(lst):
    if len(lst) <= 1:
        return lst
    
    pivot = lst[len(lst) // 2]
    left = [x for x in lst if x < pivot]
    middle = [x for x in lst if x == pivot]
    right = [x for x in lst if x > pivot]
    
    return quicksort(left) + middle + quicksort(right)


# Merge sort (recursão, if, while)
def mergesort(lst):
    if len(lst) <= 1:
        return lst
    
    mid = len(lst) // 2
    left = mergesort(lst[:mid])
    right = mergesort(lst[mid:])
    
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# Busca em profundidade em grafo (recursão, if, for)
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(start)
    result = [start]
    
    if start not in graph:
        return result
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            result.extend(dfs(graph, neighbor, visited))
    
    return result


# Verifica se número é primo (for, if)
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    
    return True


# Gera números primos até n (for, if)
def primes_up_to(n):
    if n < 2:
        return []
    
    primes = []
    for num in range(2, n + 1):
        is_p = True
        for p in primes:
            if p * p > num:
                break
            if num % p == 0:
                is_p = False
                break
        if is_p:
            primes.append(num)
    
    return primes