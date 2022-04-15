def countdown(x):
    if x == 0:
        print("countdown ended")
    else:
        print(f'{x} ..', end=' ')
        countdown(x - 1)


countdown(5)
