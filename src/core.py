from random import randrange

number_of_products = 100

def generate_wc_product(product_id):
    return {"id": product_id, "supply": randrange(1, 10)}

  
def generate_cc_product(product_id):
    return {"id": product_id, "demand": randrange(1, 10)}


def generate_wc_products(num_of_products):
    to_return = []
    for i in list(range(1, num_of_products)):
        to_return.append(generate_wc_product(i))
    return to_return


def generate_wc(wc_id, number_of_people, number_of_products):
  return {"id": wc_id,
          "population": number_of_people,
          "products": generate_wc_products(number_of_products)}

# list(range(1, randrange(2, 10)))

#(defn generate-cc [cc-id number-of-people number-of-products]
#  (hash-map :id cc-id
#            :population number-of-people
#            :products (mapv generate-cc-products (range 1 (inc number-of-products)))))

