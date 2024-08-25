from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return '''
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content, initial-scale=1.0">
    <title>21BCE7822</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Lexend:wght@100..900&display=swap');

        body {
            background-color: #e8f5e9;
            font-family: "Lexend", sans-serif;
            margin: 0;
            padding: 0;
        }

        .wrapper {
            display: flex;
            justify-content: center;
            align-items: flex-start;
            margin-top: 40px;
            padding: 20px;
        }

        .input-area, .output-area {
            width: 48%;
            padding: 20px;
            background-color: #ffffff;
            border-radius: 8px;
            box-shadow: 0 3px 6px rgba(0, 0, 0, 0.1);
            margin: 0 10px;
        }

        .input-area h1, .output-area h2 {
            color: #004d40;
            margin-bottom: 15px;
        }

        .input-area textarea {
            width: 100%;
            padding: 10px;
            margin-bottom: 10px;
            border-radius: 4px;
            border: 1px solid #ccc;
            font-size: 1rem;
            box-sizing: border-box;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
        }

        .input-area button {
            width: 100%;
            padding: 10px;
            background-color: #004d40;
            color: white;
            border: none;
            border-radius: 4px;
            font-size: 1rem;
            cursor: pointer;
            transition: background-color 0.3s;
        }

        .output-area pre {
            background-color: #f1f8e9;
            padding: 10px;
            border-radius: 4px;
            white-space: pre-wrap;
            word-wrap: break-word;
        }

        .toggle-group {
            margin-top: 10px;
        }

        .toggle-group label {
            display: block;
            margin-bottom: 8px;
        }

        .hidden {
            display: none;
        }
    </style>
</head>

<body>
    <div class="wrapper">
        <div class="input-area">
            <h1>Input JSON Data</h1>
            <form id="jsonForm">
                <textarea id="jsonInput" rows="8" placeholder='Enter JSON data like {"data":["a","b","1"]}'></textarea><br>
                <button type="button" onclick="submitData()">Submit</button>
            </form>
        </div>
        <div class="output-area">
            <h2>Output Data</h2>
            <pre id="responseData"></pre>
            <div class="toggle-group">
                <label><input type="checkbox" id="showNumbers" onclick="toggleVisibility()"> Numbers</label>
                <label><input type="checkbox" id="showAlphabets" onclick="toggleVisibility()"> Alphabets</label>
                <label><input type="checkbox" id="showMaxLowercaseAlphabet" onclick="toggleVisibility()"> Highest Lowercase Alphabet</label>
            </div>
            <div id="numbersDiv" class="hidden"></div>
            <div id="alphabetsDiv" class="hidden"></div>
            <div id="maxLowercaseAlphabetDiv" class="hidden"></div>
        </div>
    </div>

    <script>
        function submitData() {
            const jsonInput = document.getElementById('jsonInput').value;
            const endpoint = '/process';

            fetch(endpoint, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: jsonInput
            })
                .then(response => response.json())
                .then(data => {
                    document.getElementById('responseData').textContent = JSON.stringify(data, null, 2);
                    document.getElementById('numbersDiv').textContent = `Numbers: ${data.numbers.join(', ')}`;
                    document.getElementById('alphabetsDiv').textContent = `Alphabets: ${data.alphabets.join(', ')}`;
                    document.getElementById('maxLowercaseAlphabetDiv').textContent = `Highest Lowercase Alphabet: ${data.highest_lowercase_alphabet.join(', ')}`;
                })
                .catch(error => console.error('Error:', error));
        }

        function toggleVisibility() {
            document.getElementById('numbersDiv').classList.toggle('hidden', !document.getElementById('showNumbers').checked);
            document.getElementById('alphabetsDiv').classList.toggle('hidden', !document.getElementById('showAlphabets').checked);
            document.getElementById('maxLowercaseAlphabetDiv').classList.toggle('hidden', !document.getElementById('showMaxLowercaseAlphabet').checked);
        }
    </script>
</body>

</html>
'''

@app.route('/process', methods=['POST'])
def process_data():
    data = request.json.get('data', [])
    numbers = [int(item) for item in data if item.isdigit()]
    alphabets = [item for item in data if item.isalpha()]
    # Find the highest lowercase alphabet
    lowercase_alphabets = [item for item in alphabets if item.islower()]
    highest_lowercase_alphabet = [max(lowercase_alphabets)] if lowercase_alphabets else []

    response = {
        "success": True,
        "user_id": "ChintamSravanKumar",
        "email": "chintamsravankumar@gmail.com",
        "roll_number": "21BCE7822",
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_lowercase_alphabet": highest_lowercase_alphabet
    }
    return jsonify(response)

@app.route('/process', methods=['GET'])
def get_info():
    return jsonify({"status": "active"})

if __name__ == '__main__':
    app.run()
