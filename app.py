from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)


def generate_strong_password(length, use_upper, use_lower, use_digits, use_symbols):
    char_pool = ""

    if use_upper:
        char_pool += string.ascii_uppercase
    if use_lower:
        char_pool += string.ascii_lowercase
    if use_digits:
        char_pool += string.digits
    if use_symbols:
        char_pool += "!@#$%^&*()-_+="

    if not char_pool:
        return "Select at least one Character Type!"

    password = ''.join(random.choices(char_pool, k=length))
    return password


@app.route('/', methods=['GET', 'POST'])
def index():
    password = ""
    length = 12
    use_upper = True
    use_lower = True
    use_digits = True
    use_symbols = False

    if request.method == 'POST':
        try:
            length = int(request.form.get('length', 12))

            if length < 8 or length > 30:
                password = "Error: Length must be between 8 and 30."

            use_upper = 'upper' in request.form
            use_lower = 'lower' in request.form
            use_digits = 'digits' in request.form
            use_symbols = 'symbols' in request.form

            if "Error" not in password:
                password = generate_strong_password(
                    length, use_upper, use_lower, use_digits, use_symbols
                )

        except ValueError:
            password = "Invalid length! Must be a number."
            length = 12

    return render_template(
        'index.html',
        generated_password=password,
        length=length,
        use_upper=use_upper,
        use_lower=use_lower,
        use_digits=use_digits,
        use_symbols=use_symbols
    )


# if __name__ == '__main__':
    # app.run(debug=True)
