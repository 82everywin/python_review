def up_down(input_num,correct):
    if input_num>correct:
        return "down"
    elif input_num<correct:
        return "up"
    elif input_num==correct:
        return "정답!"

