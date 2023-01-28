from random import randrange
from math import floor

number_of_products = 1000
population = 1000000

# wc_id,wc_population,
# wc_id,product_id,product_supply
# cc_id,cc_population
# cc_id,product_id,product_demand

def create_nationish(population_size, num_of_products):
    wc_id = 1
    cc_id = 2
    p_counter = 0
    wc_population_file = open("wc_populations.txt", "a")
    cc_population_file = open("cc_populations.txt", "a")
    wc_product_file = open("wc_products.txt", "a")
    cc_product_file = open("cc_products.txt", "a")
    while (p_counter < population_size):
        cc_population = randrange(2, 150)
        wc_population = floor(cc_population * 0.65)
        wc_population_file.write(str(wc_id) + "," + str(wc_population) + "\n")
        cc_population_file.write(str(cc_id) + "," + str(cc_population) + "\n")
        for product_id in list(range(1, num_of_products)):
            wc_product_file.write(str(wc_id) + "," + str(product_id) + "," + str(randrange(1, 11)) + "\n")
            cc_product_file.write(str(cc_id) + "," + str(product_id) + "," + str(randrange(1, 11)) + "\n")
        p_counter = p_counter + cc_population
        wc_id = wc_id + 2
        cc_id = cc_id + 2
    wc_population_file.close()
    cc_population_file.close()
    wc_product_file.close()
    cc_product_file.close()

if __name__ == "__main__":
    create_nationish(population, number_of_products)
