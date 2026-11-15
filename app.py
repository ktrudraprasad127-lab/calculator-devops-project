
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = None
    error = None

    if request.method == "POST":
        try:
            numbers_input = request.form.get("numbers", "")
            operation = request.form.get("operation", "")

            raw_numbers = [n.strip() for n in numbers_input.split(",")]

            if not numbers_input.strip() or any(n == "" for n in raw_numbers):
                raise ValueError

            numbers = [float(n) for n in raw_numbers]

            if operation == "add":
                result = sum(numbers)

            elif operation == "subtract":
                result = numbers[0]
                for n in numbers[1:]:
                    result -= n

            elif operation == "multiply":
                result = 1
                for n in numbers:
                    result *= n

            elif operation == "divide":
                result = numbers[0]
                for n in numbers[1:]:
                    if n == 0:
                        raise ZeroDivisionError
                    result /= n

            else:
                error = "Please select a valid operation."

        except ZeroDivisionError:
            error = "Cannot divide by zero."

        except ValueError:
            error = "Please enter valid numbers separated by commas."

    return render_template("index.html", result=result, error=error)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
