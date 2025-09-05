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

while game_on:
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")

    data = pandas.read_csv("50_states.csv")
    states_data = data["state"].to_list()

    print()

    if answer_state in states_data:
        row_x = data.loc[data["state"] == answer_state, "x"].iloc[0]
        row_y = data.loc[data["state"] == answer_state, "y"].iloc[0]
        row_x, row_y = int(row_x), int(row_y)
        #print(row_x, row_y)
        print(answer_state)
        write_name.name_on_screen(int(row_x), int(row_y), str(answer_state))

screen.exitonclick()

