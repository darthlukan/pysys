# -*- coding: utf-8 -*-


def test_find_over_zero(find):
    if find > 0:
        return True
    else:
        print "We can't find sqroots for integers zero or less."
        return False


def get_find(find):
    find = input("Which number do we want the sqroot for?: ")
    return find


def start_guessing(find, guess, c_guess, counter):

    if counter > 0:
        counter = counter
    else:
        counter = 0

    if c_guess > 1:
        start = c_guess
    else:
        start = 1

    for i in range(start, find):
        c_guess += i
        if (i * i) == find:
            guess = i
            return guess
        else:
            counter += 1
            if counter > 500:
                print "We've run too many times, breaking"
                guess = "FAILED!"
                return guess
            else:
                start_guessing(find, guess, c_guess, counter)
    return guess


def main():

    guess = 0
    c_guess = 0

    find = 0
    find = get_find(find)

    if test_find_over_zero(find):
        final_guess = start_guessing(find, guess, c_guess, counter=0)
        response = "Our best guess is %d" % final_guess
        return response
    else:
        find = get_find(find)

if __name__ == '__main__':
    main()
