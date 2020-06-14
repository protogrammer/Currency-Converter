
Currencies = {
	'рубль': 1.0,
	'доллар': 74.0,
}

def convertCurrency(From: str, To: str, amount: float) -> float:
	if not (From in Currencies and To in Currencies):
		raise
	return amount * Currencies[From] / Currencies[To]

print('Введите название вашей валюты.')
currencyFrom = input().split()[0].lower()
while not currencyFrom in Currencies.keys():
	print('Неизвестная валюта. Попробуйте снова.')
	currencyFrom = input().split()[0].lower()
	
print('Введите название желаемой валюты.')
currencyTo = input().split()[0].lower()
while not currencyTo in Currencies.keys():
	print('Неизвестная валюта. Попробуйте снова.')
	currencyTo = input().split()[0].lower()

print('Введите сумму.')
amount = 0
while True:
	try:
		amount = float(input())
		break
	except:
		print('Неправильный формат числа. Попробуйте снова.')
	
print(f'{convertCurrency(currencyFrom, currencyTo, amount):.2f}')