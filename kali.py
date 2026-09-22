from flask import Flask, render_template

app = Flask(__name__)

# Kaydka ereyada Slang-ka (Dictionary)
slangs = [
    
    {
        "word": "No cap",
        "meaning": "Been maaha / Runbaan sheegayaa",
        "example": "That food was amazing, no cap!"
    },
    
    {
        "word": "Ghost",
        "meaning": "Inaad duqa ama qof aad wada xiriiri jirteen iska jaratid",
        "example": "She stopped texting me, I think she ghosted me."
    },
    {
        "word": "Flex",
        "meaning": "Inaad wixii aad leedahay ku kibri ama ku faanro",
        "example": "He bought a new car just to flex."
    }
]

# 1. Bixi marinka ugu horeeya (Homepage Route)
@app.route('/')
def home():
    return render_template('index.html', slangs=slangs)

# 2. Shuruudda si koodka uu toos u ordo
if __name__ == '__main__':
    app.run(debug=True)