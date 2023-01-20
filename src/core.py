from random import randrange
from math import floor
from os.path import exists
import json

number_of_products = 300
population = 1000000

def generate_wc_product(product_id):
    return {"id": product_id, "supply": randrange(1, 11)}

  
def generate_cc_product(product_id):
    return {"id": product_id, "demand": randrange(1, 11)}


def generate_wc_products(num_of_products):
    to_return = []
    for i in list(range(1, num_of_products)):
        to_return.append(generate_wc_product(i))
    return to_return


def generate_wc(wc_id, number_of_people, num_of_products):
  return {"id": wc_id,
          "population": number_of_people,
          "products": generate_wc_products(num_of_products)}


def generate_cc_products(num_of_products):
    to_return = []
    for i in list(range(1, num_of_products)):
        to_return.append(generate_cc_product(i))
    return to_return


def generate_cc(cc_id, number_of_people, num_of_products):
    return {"id": cc_id,
            "population": number_of_people,
            "products": generate_cc_products(num_of_products)}


def create_nationish(population_size, num_of_products):
    wc_id = 1
    cc_id = 2
    p_counter = 0
    wcs_to_return = []
    ccs_to_return = []
    while (p_counter < population_size):
        cc_population = randrange(2, 150)
        wc_population = floor(cc_population * 0.65)
        p_counter = p_counter + 1
        wcs_to_return.append(generate_wc(wc_id, wc_population, number_of_products))
        ccs_to_return.append(generate_cc(cc_id, cc_population, number_of_products))
        wc_id = wc_id + 2
        cc_id = cc_id + 2
        p_counter = p_counter + cc_population
    return {"wcs": wcs_to_return,
            "ccs": ccs_to_return}

if __name__ == "__main__":
    if exists("./nationish.json"):
       with open('nationish.json', 'r') as openfile:
           nationish = json.load(openfile)
       print(len(nationish["ccs"]), len(nationish["wcs"]))
    else:
       nationish = create_nationish(population, number_of_products)
       json_object = json.dump(nationish, indent=4)
       with open("nationish.json", "w") as outfile:
           outfile.write(json_object)

