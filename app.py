import random
from flask import Flask, request, jsonify

app = Flask(__name__)

sem_1 = []
sem_2 = []
responses = {}

# Function to greet the user
def greet():
    greetings = ["Hello!", "Hi there!", "Hey!", "Greetings!", "Howdy!"]
    return random.choice(greetings)

# Function for getting the bot's name
def get_bot_name():
    return "LittleBot"

# Function to store the data
def data_stored():
    global sem_1, sem_2, responses
    sem_1 = [["micro", "KG Sir",
              "1-> Sir is good",
              "2-> But KG sir achen mane syllabus er size hobe huge and sir bullet train er thekeo fast poraben",
              "3-> Do not bunk his classes",
              "4-> Internal er prosno anek tough deben jodio home assignment but sir pore ektu hints o deben",
              "5-> Semester er prosno o standard hobe but sir thik sem-1 er last class e syllabus e important jinis potro bolben but ultimately hardly 10% syllabus kombe",
              "6-> BUT exam er thik 4 din age sir ekta class neben sekhane ekdom jei part gulo theke question asbe sudhu seiguloi bole deben",
              "7-> Sir er notes e anek proof thake but oto besi lagbe na,jeigulo lagbe sir seigulo bole deben just 4 days before exam",
              "8-> Sir puro chesta koren jate sobai jno bhalo marks pai"],
             ["macro", "ACH Sir",
              "1-> Easiest paper to score very good marks",
              "2-> Ekdom precise and to the point answers sir pochondo koren",
              "3-> Question 3 marks er hok or 8 marks er; jotota answer thik  exactly tototai likhbi",
              "4-> Besi likhlei sir marks kete deben(anek marks kete deben tai pls don't write extra)",
              "5-> Internal e offline exam neben tai semester suru thekei macro pora start koris"],
             ["matheco", "BR Sir",
              "1-> Paper ta sudhu namei math-eco; maths anek kom e asbe ,maximum theory e asbe",
              "2-> Sir jta class e koraben,sekhan thekei exam e deben",
              "3-> Ekta super senior der notes available ache, amader batch theke karur theke tora peye o jabi but ote anek extra jinis ache,oto kichu porte lagbe na",
              "4-> Only jta Sir poraben toder batch der sudhu seiguloi porte hobe",
              "5-> Internal amader home assignment diyechilen, so no chap"],
             ["indianeco", "SG/MC Mam",
              "1-> Mukhosto kore bomi korte hobe exam e",
              "2-> You can bunk indian eco classes",
              "3-> Internal er jonne home assignment debe so use chatgpt karon mam avg e 7-8 bosabe sobaike"],
             ["ecotrix", "AS Mam/PD Sir",
              "1-> Dujonei bhalo poran khub",
              "2-> If you bunk then your loss",
              "3-> Sir/Mam class e ja poraben seta thekei question asbe exam e",
              "4-> Internal niye no chap, easy prosnoi korben",
              "5-> PD sir proofs gulo pochondo koren segulo exam e deben but AS man proofs deya pochondo koren na and seta mam nijeo class e bolben",
              "5-> Semester suru thekei pora start koris ei paper tao karon offline e IA dite hobe"],
             ["general","General_Tips",
              "1-> Sem 1 er marks khub important,otar basis e sem3 te paper choose korte parbi so bhalo kore sem1 e poris",
              "2-> Try to get atleast 6 sgpa , karon anek company sudhu sei student der e allow korbe jader atleast 6 ache",
              "3-> Sem 3 te GE subject e development na nite chaile, english o nite paris. Sudhu every wednesday college street campus jete hobe, Wednesday sudhu GE class e hoi, (Syllabus- Film review + Film History)"]]

    sem_2 = [
        ["micro", "SBH Sir",
         "1-> Do not bunk his classes(NEVER!!!)",
         "2-> Sir er IA ta open book exam hoi",
         "3-> Ei paper tai besi mukhosto korte hoi na so good paper, marks tolar jonne"],
        ["macro", "KM Sir",
         "1-> Syllabus kom etar",
         "2-> IA ta home assignment,so use chatgpt, avg e 6-7 debe ",
         "3-> Motamuti sir ja poraben seta likhe dile thik thak marks diye deben"],
        ["history", "IM Mam",
         "1-> Life e jei subject ta sob theke bekar lage, tar thekeo bekar ekta paper porar jonne ready hoi jaa",
         "2-> IA offline hobe so chap",
         "3-> Syllabus o anek "],
        ["deveco", "ARD Mam/AM Sir",
         "1-> Sir/Mam dujonei bhalo poran ",
         "2-> Try not to bunk if possible, karon class thikthak follow korlei hoi jabe",
         "3-> IA will be offline but relatively easy"],
        ["ecotrix", "PD Sir",
         "1-> Sir er bepar e agei bolechi so r kichu bolar nei.",
         "2-> Hoi jabe ei paper ta, easy e(but tai bole sem 3 te eta niye nis na)"]
    ]

    responses = {
        "sem 1": sem_1,
        "sem 2": sem_2
    }

# Function for handling talk
def talk(semester, paper_choice):
    semester = semester.lower()
    if semester not in responses:
        return "Invalid semester. Please choose 'sem 1' or 'sem 2'."
    for item in responses[semester]:
        if paper_choice == item[0].lower():
            return "\n".join(item[1:])
    return "Wrong Choice!!!"

@app.route("/", methods=["GET"])
def home():
    return "Welcome to LittleBot's Web Interface!"

@app.route("/chat", methods=["POST"])
def chat():
    data_stored()
    data = request.json
    semester = data.get("semester")
    paper_choice = data.get("paper")
    if not semester or not paper_choice:
        return jsonify({"error": "Please provide 'semester' and 'paper' in the request body."}), 400
    response = talk(semester, paper_choice)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
