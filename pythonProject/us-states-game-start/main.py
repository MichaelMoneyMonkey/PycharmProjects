import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")

guessed_states = []

guessed_correctly = 0
# 4. loop to keep guessing till 50
while guessed_correctly < 50:
    answer_state = screen.textinput(title=f"{guessed_correctly}/50 States correct", prompt="What's another state's name?")
    # 1. Convert answer to title case
    answer = answer_state.title()
    print(answer)

    # 2. Check is answer is in the column state
    correct = answer in data.values
    print(correct)

    if answer == "Exit":
        all_states = data.state.to_list()
        # # optie 1
        # missing_states = set(all_states) - set(guessed_states)
        # # optie 2
        # missing_states = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        #  optie 3 (optie 2 verkort)
        missing_states = [state for state in all_states if state not in guessed_states]

        print(missing_states)

        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")

        break

    # 3. Write correct answer of map
    if correct == True:
        guessed_states.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer)
        guessed_correctly += 1
        print(guessed_states)











screen.exitonclick()