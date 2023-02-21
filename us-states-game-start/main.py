import turtle
import pandas
screen = turtle.Screen()
screen.title("USA states game")
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
ans = turtle.Turtle()
ans.penup()
ans.hideturtle()
answers = []
game = 0

all_states = data.state.to_list()
while game != 50:

    answer_state = screen.textinput(title=f"Guess the state, score {game}/50", prompt="Whats another states name                ").title()
    if answer_state == "Exit":
        states_list = []
        for x in all_states:
            if x not in answers:
                states_list.append(x)
        df = pandas.DataFrame(states_list)
        df.to_csv("pe.csv")
        break
    if answer_state in data.values:
        answers.append(answer_state)
        ans_index = data[data['state'] == answer_state].index.values
        ind = ans_index[0]
        ans_x = (data._get_value(ind, 'x'))
        ans_y = (data._get_value(ind, 'y'))
        ans.goto(ans_x,ans_y)
        ans.write(f"{answer_state}",align = "center")
        game += 1
        ans.home()
    else:
        ans.home()

