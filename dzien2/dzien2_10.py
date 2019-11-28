# napisz program, ktory wyswietli 6 losowych i nie powtarzających się liczb

from random import sample

population = range(1,50)
quantity = 6
result = sample(population,quantity)
print(result)
result.sort()
print(result)
