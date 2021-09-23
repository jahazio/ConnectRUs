from flask import Flask
from matplotlib import pyplot as plt
import pendulum
import numpy as np
import pandas as pd

# Create a flask app
app = Flask(
  __name__,
  template_folder='templates',
  static_folder='static'
)

# Index page
@app.route('/')
def hello():
  return "Hello World!"

#Amanda's HTTP Request
@app.route("/number/<input>")
def number(input):
  input = int(input)
  if (input%2==0):
    return "even!"
  else:
    return "odd!"

#Sandra's HTTP Request
def ftoc(ftemp):
   return (ftemp-32.0)*(5.0/9.0)

@app.route('/ftoc/<ftempString>')
def convertFtoC(ftempString):
    ftemp = 0.0
    try:
        ftemp = float(ftempString)
        ctemp = ftoc(ftemp)
        return ftempString + "° degree Farenheit is " + str(ctemp) +" in Celsius "
    except ValueError:
        return "Sorry.  Could not convert " + ftempString + " to a number"

#Jonathan's HTTP Request
def ktomi(kilo):
  return (kilo*.621371)

@app.route('/ktomi/<kilometers>')
def convertKtoMi(kilometers):
  try:
    kilo=float(kilometers)
    mi=ktomi(kilo)
    return kilometers + " kilometers is " + str(mi) + " miles."
  except ValueError:
      return "Sorry. Could not convert " + kilometers + " to miles."

#Julia's HTTP Request
@app.route("/factorial/<n>")
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("Input a number to compute the factiorial : "))
print(factorial(n))

#Chelsea's HTTP Request
@app.route("/square/<n>")
def square(n):
    n = int(n)
    n_sq = n ** 2
    return "The square of " + str(n) + " is " + str(n_sq)

# Amanda's A4 code
@app.route("/timezone")
def timezone():
    local = pendulum.now()
    paris_time = pendulum.timezone('Europe/Paris').convert(pendulum.now('UTC'))
    start = pendulum.today()
    end = pendulum.datetime(2021, 12, 18)
    period = pendulum.period(start, end)
    return "Your time is " + local.to_day_datetime_string() + "</br> In Paris it is " + paris_time.to_day_datetime_string() + "</br>" + str(period.days) + " day until end of semester"

#Sandra's A4 code
@app.route('/arrays/<row>/<col>')
def arrays(row, col):
    r = int(row)
    c = int(col)
    z = np.zeros((r, c))
    return "An array initialized with all zeros:</br>" + str(z)

#Julia's A4 code
@app.route("/table")
def table():
    data = np.array([['', 'Col1', 'Col2'],
                     ['Row1', 1, 2],
                     ['Row2', 3, 4]])

    df = (pd.DataFrame(data=data[1:, 1:],
                       index=data[1:, 0],
                       columns=data[0, 1:]))

    return str(df)

# Chelsea's A4 code
@app.route("/plot")
def plot():
    x_values = [1, 2, 3, 4]
    y_values = [4, 3, 2, 1]

    plt.plot(x_values, y_values, color="navy")
    plt.title("Chelsea's energy level of the day")
    plt.xlabel("x values")
    plt.ylabel("y values")
    return str(plt.show())

#Jonathan's A4 code
@app.route('/parse')
def parse():
    url = "https://www.tutorialspoint.com/index.htm"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    return "Website titles is " + str(soup.title.text)


app.run(host = "0.0.0.0")
