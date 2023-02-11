from random import randrange
from math import floor
from guppy import hpy
from time import perf_counter
import sqlite3

number_of_products = 100000
population = 1000000

# wc_id,wc_population,
# wc_id,product_id,product_supply
# cc_id,cc_population
# cc_id,product_id,product_demand

def load_data_to_sqlite_db(file_to_use):
    cc_pop_file = open(file_to_use, 'r')
    con = sqlite3.connect("pe_ifb_compute.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE products(council_type, council_id, product_id, quantity)")
    cur.execute("CREATE INDEX product_id_index on products(product_id)")
    while True:
        L = cc_pop_file.readline()
        if not L:
            break
        d = L.strip().split(",")
        cur.execute("INSERT INTO products VALUES('cc', ?, ?, ?)", [d[0], d[1], d[2]])
        con.commit()
    cc_pop_file.close()
    con.close() 

def ifm():
    cc_pop_file = open('cc_products.txt', 'r')
    r = {}
    i = 0
    while True:
        L = cc_pop_file.readline()
        i = i + 1

        if not L:
            break

        d = L.strip().split(",")
        if i % 100000000 == 0: #mod 100 million
            print(i)

        try:
            r[int(d[1])] = r[int(d[1])] + int(d[2])
        except:
            r[int(d[1])] = int(d[2])
    cc_pop_file.close()
    return r

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

def analyze_heap():
    perf_counter()
    heap = hpy()

    print("Heap Status At Starting : ")
    heap_status1 = heap.heap()
    print("Heap Size : ", heap_status1.size, " bytes\n")
    print(heap_status1)

    heap.setref()
    print("\nHeap Status After Setting Reference Point : ")
    heap_status2 = heap.heap()
    print("Heap Size : ", heap_status2.size, " bytes\n")
    print(heap_status2)

    create_nationish(population, number_of_products)

    print("\nHeap Status After Creating Few Objects : ")
    heap_status3 = heap.heap()
    print("Heap Size : ", heap_status3.size, " bytes\n")
    print(heap_status3)
    print("\nMemory Usage After Creation Of Objects : ", heap_status3.size - heap_status2.size, " bytes")
    perf_counter()

if __name__ == "__main__":
    load_data_to_sqlite_db('cc_products.txt')
    #cc_p = ifm()
    # print(cc_p)
    #analyze_heap()
