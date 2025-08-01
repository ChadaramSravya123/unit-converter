from flask import Flask, render_template, request

app = Flask(__name__)

# Conversion rates for length and weight
length_units = {
    'millimeter': 0.001,
    'centimeter': 0.01,
    'meter': 1,
    'kilometer': 1000,
    'inch': 0.0254,
    'foot': 0.3048,
    'yard': 0.9144,
    'mile': 1609.34
}

weight_units = {
    'milligram': 0.000001,
    'gram': 0.001,
    'kilogram': 1,
    'ounce': 0.0283495,
    'pound': 0.453592
}

# Temperature conversion function
def convert_temperature(value, from_unit, to_unit):
    if from_unit == "celsius":
        if to_unit == "fahrenheit":
            return (value * 9/5) + 32
        elif to_unit == "kelvin":
            return value + 273.15
    elif from_unit == "fahrenheit":
        if to_unit == "celsius":
            return (value - 32) * 5/9
        elif to_unit == "kelvin":
            return (value - 32) * 5/9 + 273.15
    elif from_unit == "kelvin":
        if to_unit == "celsius":
            return value - 273.15
        elif to_unit == "fahrenheit":
            return (value - 273.15) * 9/5 + 32
    return value

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        try:
            value = float(request.form["value"])
            from_unit = request.form["from_unit"]
            to_unit = request.form["to_unit"]
            conversion_type = request.form["conversion_type"]

            if conversion_type == "length":
                value_in_meters = value * length_units[from_unit]
                converted_value = value_in_meters / length_units[to_unit]
                result = f"{value} {from_unit} = {converted_value:.4f} {to_unit}"

            elif conversion_type == "weight":
                value_in_kg = value * weight_units[from_unit]
                converted_value = value_in_kg / weight_units[to_unit]
                result = f"{value} {from_unit} = {converted_value:.4f} {to_unit}"

            elif conversion_type == "temperature":
                converted_value = convert_temperature(value, from_unit, to_unit)
                result = f"{value}° {from_unit.capitalize()} = {converted_value:.2f}° {to_unit.capitalize()}"
        except ValueError:
            result = "Invalid input! Please enter a number."

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
