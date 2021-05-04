# created a project based on a task using simple_draw library

import simple_draw as sd

N = 20
sd.resolution = (1200, 600)
snowflakes_param, fallen = [], []

# created started list of snowflakes
def flake_add(param, N):
    for i in range(N):
        x = sd.random_number(100, 1200)
        y = sd.random_number(500, 800)
        length = sd.random_number(5, 25)
        param.append([x, y, length])


flake_add(snowflakes_param, 40)


# implementation
def snowflake():
    ground_level = 50
    k = 0
    while True:
        sd.start_drawing()
        for i in snowflakes_param:
            x = i[0]
            y = i[1]
            point = sd.get_point(x, y)
            snowflake_length = i[2]
            sd.snowflake(center=point, length=snowflake_length, color=sd.background_color)
            i[1] -= sd.random_number(0, 20)
            i[0] += sd.random_number(-20, 20)
            point_1 = sd.get_point(i[0], i[1])
            sd.snowflake(center=point_1, length=snowflake_length, color='white')
            if y < ground_level:
                ind = snowflakes_param.index(i)
                fallen.append(snowflakes_param.pop(ind))
                flake_add(snowflakes_param, 1)
                k += 1
        if k >= 10:
            ground_level += 5
            k = 0
        sd.finish_drawing()
        sd.sleep(0.1)
        if sd.user_want_exit():
            break


snowflake()

sd.pause()