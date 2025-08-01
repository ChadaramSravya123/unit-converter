Unit Converter – Single Page Flask App
A simple web-based Unit Converter built with Python (Flask) that allows users to convert between different units of Length, Weight, and Temperature in a single page.

Features
Convert Length, Weight, and Temperature in one interface.

Dropdown menu for selecting conversion type.

Automatic update of units based on conversion type.

Instant calculation and display of results.

Responsive, clean, and easy-to-use design.

Technologies Used
Backend: Python 3, Flask

Frontend: HTML5, CSS3, JavaScript

Styling: Custom CSS

Conversion Supported
Length
millimeter ↔ centimeter ↔ meter ↔ kilometer ↔ inch ↔ foot ↔ yard ↔ mile

Weight
milligram ↔ gram ↔ kilogram ↔ ounce ↔ pound

Temperature
Celsius ↔ Fahrenheit ↔ Kelvin

Installation & Setup
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/<your-username>/unit-converter.git
cd unit-converter
2️⃣ Create Virtual Environment & Install Dependencies
bash
Copy
Edit
python -m venv venv
# Activate venv:
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

pip install flask
3️⃣ Run the App
bash
Copy
Edit
python app.py
4️⃣ Open in Browser
cpp
Copy
Edit
http://127.0.0.1:5000
Usage
Select conversion type (Length, Weight, Temperature).

Enter the value you want to convert.

Choose From Unit and To Unit.

Click Convert to see the result.

Project Structure
pgsql
Copy
Edit
unit-converter/
│
├── app.py              # Flask backend with conversion logic
├── templates/
│   └── index.html      # Main HTML page
├── static/
│   └── style.css       # Styling for the page
└── README.md           # Project documentation
Example
Input:

makefile
Copy
Edit
Type: Length
Value: 20
From: foot
To: centimeter
Output:
20 foot = 609.6000 centimeter

Future Improvements
Add support for Volume, Area, and Time conversions.

Add dark mode for better user experience.

Add mobile-friendly responsive design.
