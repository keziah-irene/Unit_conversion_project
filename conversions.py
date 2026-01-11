def length(value, from_unit, to_unit): 
    units = ['Kilometer', 'Meter', 'Centimeter', 'Millimeter', 'Foot', 'Inch']
    factors = [1000, 1, 0.01, 0.001, 0.3048, 0.0254] #converted to meters

    if from_unit in units and to_unit in units: #checks if both units are in the list
        from_index = units.index(from_unit) # stores index position of from_unit 
        to_index = units.index(to_unit) # stores index position of to_unit 

        if from_unit == to_unit: 
            return value        
        return value * factors[from_index] / factors[to_index]
    
    else:
        return "Invalid Unit"

def mass(value, from_unit, to_unit):
    units = ['Kilograms', 'Grams', 'Milligrams', 'Pounds', 'Ounce']
    factors = [1, 1000, 1_000_000, 2.20462, 35.274]  # Converted to kilograms

    if from_unit in units and to_unit in units:
        from_index = units.index(from_unit)
        to_index = units.index(to_unit)

        if from_unit == to_unit:
            return value
        return value * (1 / factors[from_index]) * factors[to_index]
   
    else:
        return "Invalid Unit"

def temperature(value, from_unit, to_unit): 
    if from_unit == to_unit:
        return value
    if from_unit == 'Celsius':
        if to_unit == 'Fahrenheit':
            return value * 9/5 + 32
        elif to_unit == 'Kelvin':
            return value + 273.15
    elif from_unit == 'Fahrenheit':
        if to_unit == 'Celsius':
            return (value - 32) * 5/9
        elif to_unit == 'Kelvin':
            return (value - 32) * 5/9 + 273.15
    elif from_unit == 'Kelvin':
        if to_unit == 'Celsius':
            return value - 273.15
        elif to_unit == 'Fahrenheit':
            return (value - 273.15) * 9/5 + 32
    return "Conversion Error"

def speed(value, from_unit, to_unit):
    units = ['Meter per second', 'Kilometer per hour', 'Kilometer per second', 'Miles per hour']
    factors = [1, 0.277778, 1000, 0.44704] # converted to meter per second

    if from_unit in units and to_unit in units:
        from_index = units.index(from_unit)
        to_index = units.index(to_unit)

        if from_unit == to_unit:
            return value
        return value * factors[from_index] / factors[to_index]
   
    else:
        return "Invalid Unit"

def time(value, from_unit, to_unit):
    units = ['Year', 'Months', 'Days', 'Hours', 'Minutes', 'Seconds', 'Milliseconds']
    factors = [31_536_000_000, 2_629_746_000, 86_400_000, 3_600_000, 60_000, 1_000, 1]  # converted to milliseconds

    if from_unit in units and to_unit in units:
        from_index = units.index(from_unit)
        to_index = units.index(to_unit)

        if from_unit == to_unit:
            return value
        return value * factors[from_index] / factors[to_index]
   
    else:
        return "Invalid Unit"

def data(value, from_unit, to_unit): 
    units = ['Terabyte', 'Gigabyte', 'Megabyte', 'Kilobyte', 'Byte']
    factors = [1_099_511_627_776, 1_073_741_824, 1_048_576, 1_024, 1] # converted to bytes

    if from_unit in units and to_unit in units:
        from_index = units.index(from_unit)
        to_index = units.index(to_unit)

        if from_unit == to_unit:
            return value
        return value * factors[from_index] / factors[to_index]
 
    else:
        return "Invalid Unit"
