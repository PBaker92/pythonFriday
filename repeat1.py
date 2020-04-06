def repeat (how_many_times, the_string):
    result = ""

    while how_many_times > 0:
        #do something??
        #print(the string)
        result += the_string
        how_many_times -= 1
    return result

#a_dog_says = repeat(5,"woof")
another_dog_says = repeat(3, a_dog_says)