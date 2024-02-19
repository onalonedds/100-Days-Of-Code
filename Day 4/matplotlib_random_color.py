import matplotlib.colors as mcolors
import turtle_draws_heart
def random_color_generator():
    color = random.choice(list(mcolors.CSS4_COLORS.keys()))
    return color

random_color = random_color_generator()
print(random_color)