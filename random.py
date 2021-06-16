import random

# this ensures we get the same results every time
random.seed(10) 

four_uniform_randoms = [random.random() for _ in range(4)]
# >> [0.5714025946899135, 0.4288890546751146, 0.5780913011344704, 0.20609823213950174]

random.shuffle(four_uniform_randomsz)
#>> [0.5780913011344704, 0.5714025946899135, 0.4288890546751146, 0.20609823213950174]

choice_one = random.choice(four_uniform_randoms)
# >> 0.5780913011344704

random_float_between_two_numbers = random.uniform(20,40);
# >> 49.58668277296182

# loto 6
loto_numbers = range(1,44)
winning_numbers = random.sample(loto_numbers, 6)
winning_numbers.sort();
# >> [5, 16, 21, 24, 32, 34]
