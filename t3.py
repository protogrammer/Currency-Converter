from functools import reduce

def processCurrencyName(s: str) -> str:
	return reduce(lambda s1, s2: s1+s2, s.split(), '').lower()

Currencies = {
	processCurrencyName('рубль'): 1.0,
	processCurrencyName('доллар'): 69.0,
	processCurrencyName('доллар США'): 69.0,
	processCurrencyName('евро'): 78.5,
	processCurrencyName('Австралийский доллар'): 48.0,
	processCurrencyName('Белорусский рубль'): 29.1,
	processCurrencyName('гривна'): 26.0,
	processCurrencyName('фунт'): 87.7,
	processCurrencyName('фунт стерлингов'): 87.7,
	processCurrencyName('фунт стерлингов Соединенного королевства'): 87.7,
}

def convertCurrency(From: str, To: str, amount: float) -> float:
	if not (From in Currencies and To in Currencies):
		raise
	return amount * Currencies[From] / Currencies[To]

print('Введите название вашей валюты.')
currencyFrom = processCurrencyName(input())
while not currencyFrom in Currencies.keys():
	print('Неизвестная валюта. Попробуйте снова.')
	currencyFrom = processCurrencyName(input())
	
print('Введите название желаемой валюты.')
currencyTo = processCurrencyName(input())
while not currencyTo in Currencies.keys():
	print('Неизвестная валюта. Попробуйте снова.')
	currencyTo = processCurrencyName(input())

print('Введите сумму.')
amount = 0
while True:
	try:
		amount = float(input())
		break
	except:
		print('Неправильный формат числа. Попробуйте снова.')
	
print(f'{convertCurrency(currencyFrom, currencyTo, amount):.2f}')