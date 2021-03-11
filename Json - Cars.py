import json

data = {'car': []}
data['car'].append({
    'brand': 'Volkswagen',
    'model': 'Passat B5.5',
    'fuel_consumption': '6.0',
    'license_plate': 'K9182BB',
    'price_per_hour': '20'
})
data['car'].append({
    'brand': 'Audi',
    'model': 'A4 Avant',
    'fuel_consumption': '6.5',
    'license_plate': 'K4416BC',
    'price_per_hour': '30'
})
data['car'].append({
    'brand': 'Volkswagen',
    'model': 'Passat B6',
    'fuel_consumption': '6.8',
    'license_plate': 'K8690BC',
    'price_per_hour': '40'
})
data['car'].append({
    'brand': 'Opel',
    'model': 'Astra',
    'fuel_consumption': '5.2',
    'license_plate': 'X1234AB',
    'price_per_hour': '15'
})
data['car'].append({
    'brand': 'BMW',
    'model': '320',
    'fuel_consumption': '7.5',
    'license_plate': 'PB8690BP',
    'price_per_hour': '60'
})
data['car'].append({
    'brand': 'Volkswagen',
    'model': 'Golf 4',
    'fuel_consumption': '5.8',
    'license_plate': 'A2546TT',
    'price_per_hour': '25'
})
data['car'].append({
    'brand': 'Mercedes',
    'model': 'C280',
    'fuel_consumption': '8.2',
    'license_plate': 'CT1463BM',
    'price_per_hour': '50'
})
data['car'].append({
    'brand': 'Porsche',
    'model': 'Panamera',
    'fuel_consumption': '9.5',
    'license_plate': 'CA1111XX',
    'price_per_hour': '120'
})
data['car'].append({
    'brand': 'Citroen',
    'model': '407',
    'fuel_consumption': '5.5',
    'license_plate': 'PA2587AB',
    'price_per_hour': '15'
})
data['car'].append({
    'brand': 'Audi',
    'model': 'A6',
    'fuel_consumption': '8.6',
    'license_plate': 'PB5472BK',
    'price_per_hour': '35'
})


with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)
