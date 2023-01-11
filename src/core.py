from random import randrange

number_of_products = 100

def generate_wc_products(product_id):
  return {"id": product_id, "supply": randrange(1, 10)}
  
def generate_cc_products(product_id):
  return {"id": product_id, "demand": randrange(1, 10)}


# list(range(1, randrange(2, 10)))

def generate_wc(wc_id, number_of_people, number_of_products):
  return {"id": wc_id,
          "population": number_of_people,
          "products": map(generate_wc_products, list(range(1, number_of_products)))}

#(defn generate-cc [cc-id number-of-people number-of-products]
#  (hash-map :id cc-id
#            :population number-of-people
#            :products (mapv generate-cc-products (range 1 (inc number-of-products)))))

