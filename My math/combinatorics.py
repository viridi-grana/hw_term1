def fact(n): # оно же перестановка
  if n < 0:
    return
  if n == 0:
    return 1
  return n * fact(n - 1)

def sochetanie(m, n):
  if 0 <= m <= n:
    return fact(n) / (fact((n - m)) * fact(m))
  else:
    return None

def razmeshenie(m, n):
  if 0 <= m <= n:
    return sochetanie(m, n) * fact(m)
  else:
    return None

if __name__ == '__main__':
    print('Запустите головной файл')