
Currencies = {
  'рубль': 1.0,
  'доллар': 74.0,
}

def convertCurrency(From: str, To: str, amount: float) -> float:
  if not (From in Currencies and To in Currencies.keys()):
    raise
  return amount * Currencies[From] / Currencies[To]

print('Введите сумму в рублях.')
amount = 0
while True:
  try:
    amount = float(input())
    break
  except:
    print('Неправильный формат числа. Попробуйте снова.')

print(f'{amount:.2f} рублей — это {convertCurrency("рубль", "доллар", amount):.2f} долларов.')