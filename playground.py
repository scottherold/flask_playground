from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play/')
def hello_world():
    return render_template("index.html", block_count=3, block_color="lightblue")

@app.route('/play/<num>')
def display_blocks(num):
    num = int(num)
    return render_template("index.html", block_count=num, block_color="lightblue")

@app.route('/play/<num>/<color>')
def display_colored_blocks(num,color):
    num = int(num)
    color = color
    return render_template("index.html", block_count=num, block_color=color)

if __name__ == "__main__":
    app.run(debug=True)