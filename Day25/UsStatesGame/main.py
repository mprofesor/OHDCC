import turtle
import pandas
import write_name

# Open a photo as a turtle background
# Create a window to input the state names
# Check the base to see if the given name is correct
# Use coords to determine where to put correct names (write them using turtle)

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)


#def get_mouse_click_coor(x, y):
#    print(x, y)
#
#
#turtle.onscreenclick(get_mouse_click_coor)
#turtle.mainloop()

game_on = True

correct_guessed_num = 0

correct_guessed_list = []
uncorrect_guessed_list = []

while game_on:
    answer_state = screen.textinput(title=f"Guessed correctly {correct_guessed_num}/50", prompt=f"What's another state's name? {correct_guessed_num}/50")

    data = pandas.read_csv("50_states.csv")
    states_data = data["state"].to_list()

    if answer_state in states_data:
        correct_guessed_num += 1
        row_x = data.loc[data["state"] == answer_state, "x"].iloc[0]
        row_y = data.loc[data["state"] == answer_state, "y"].iloc[0]
        row_x, row_y = int(row_x), int(row_y)
        #print(row_x, row_y)
        print(answer_state)
        write_name.name_on_screen(int(row_x), int(row_y), str(answer_state))
        correct_guessed_list.append(answer_state)
    else:
        uncorrect_guessed_list.append(answer_state)

    if correct_guessed_num == 50:
        score = 0

        all_guessed_list = correct_guessed_list + uncorrect_guessed_list

        for guess in all_guessed_list:
            if all_guessed_list[guess] in correct_guessed_list:
                score += 10
            elif all_guessed_list[guess] in uncorrect_guessed_list:
                score -= 5

        game_on = False


screen.exitonclick()

