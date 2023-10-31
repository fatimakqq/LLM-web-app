from flask import Flask, request, render_template
from transformers import AutoTokenizer, AutoModelForCausalLM


app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

model_name = "bigscience/bloomz-7b1"
try:
    model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype="auto", device_map="auto")
except OSError:
    print(f"Model not found locally. Downloading {model_name}...")
    model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype="auto", device_map="auto")

tokenizer = AutoTokenizer.from_pretrained(model_name)

@app.route("/", methods=["GET", "POST"])

def index():
    prompt = ""
    response = ""

    if request.method == "POST":
        prompt = request.form["prompt"]
        if len(prompt) == 0:
            prompt = ""
            response = "No prompt entered"
        
        else:
            inputs = tokenizer.encode(prompt, return_tensors="pt").to("cuda")
            max_len = 5000
            temp = 1.0

            outputs = model.generate(inputs, max_length=max_len, temperature=temp, do_sample=True)

            response = tokenizer.decode(outputs[0][len(inputs[0]):], skip_special_tokens=True)

            print("Input Prompt:", prompt)
            print("Model Response:", response)

    return render_template("index.html", prompt=prompt, response=response)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=7777)




