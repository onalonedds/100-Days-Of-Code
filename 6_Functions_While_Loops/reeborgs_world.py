# Reeborg's World - Hurdle 4
# https://reeborg.ca/index_en.html
#
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
#
# def jump():
#     turn_left()
#     wall_height = 0
#
#     while wall_on_right():
#         move()
#         wall_height += 1
#
#     turn_right()
#     move()
#     turn_right()
#
#     step_down = 0
#
#     while step_down < wall_height:
#         move()
#         step_down += 1
#
#     turn_left()
#
#
# while not at_goal():
#     if wall_in_front():
#         jump()
#     else:
#         move()