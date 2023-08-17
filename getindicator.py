import tradingeconomics as te

te.login('guest:guest')

data = te.getIndicatorData(country='mexico')

data = te.getIndicatorData(country='mexico', output_type='df')

print(data)