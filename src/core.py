from random import randrange
from math import floor
from guppy import hpy
from time import perf_counter
import sqlite3

number_of_products = 100
population = 100

# wc_id,wc_population,
# wc_id,product_id,product_supply
# cc_id,cc_population
# cc_id,product_id,product_demand

def determine_surplus_for_all_products(population_size, number_of_products):
    con = sqlite3.connect("pe_ifb_compute_" + str(population_size) + "_" + str(number_of_products) + ".db")
    cur = con.cursor()
    supply_data = cur.execute("SELECT product_id, sum(quantity) from wc_products GROUP BY product_id order by product_id;")
    print("SUPPLY DATA:")
    print(supply_data.fetchall())
    demand_data = cur.execute("SELECT product_id, sum(quantity) from cc_products GROUP BY product_id order by product_id;")
    print("DEMAND DATA:")
    print(demand_data.fetchall())
    # adjust price: (demand / supply) * previous_price
    con.close()

def load_data_to_sqlite_db(population_size, number_of_products, council_type):
    product_file = open(council_type + "_products_" + str(population_size) + "_" + str(number_of_products) + ".txt", "r")
    con = sqlite3.connect("pe_ifb_compute_" + str(population_size) + "_" + str(number_of_products) + ".db")
    cur = con.cursor()
    cur.execute("CREATE TABLE " + council_type + "_products(council_id, product_id, quantity)")
    cur.execute("CREATE INDEX " + council_type + "_product_id_index on " + council_type + "_products(product_id)")
    while True:
        L = product_file.readline()
        if not L:
            break
        d = L.strip().split(",")
        cur.execute("INSERT INTO " + council_type + "_products VALUES(?, ?, ?)", [d[0], d[1], d[2]])
        con.commit()
    product_file.close()
    con.close()

def create_nationish_files(population_size, number_of_products):
    wc_id = 1
    cc_id = 2
    p_counter = 0
    wc_population_file = open("wc_populations_" + str(population_size) + "_" + str(number_of_products) + ".txt", "a")
    cc_population_file = open("cc_populations_" + str(population_size) + "_" + str(number_of_products) + ".txt", "a")
    wc_product_file = open("wc_products_" + str(population_size) + "_" + str(number_of_products) + ".txt", "a")
    cc_product_file = open("cc_products_" + str(population_size) + "_" + str(number_of_products) + ".txt", "a")
    while (p_counter < population_size):
        cc_population = randrange(2, 150)
        wc_population = floor(cc_population * 0.65)
        wc_population_file.write(str(wc_id) + "," + str(wc_population) + "\n")
        cc_population_file.write(str(cc_id) + "," + str(cc_population) + "\n")
        for product_id in list(range(1, number_of_products + 1)):
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

    create_nationish_files(population, number_of_products)
    load_data_to_sqlite_db(population, number_of_products, 'wc')
    load_data_to_sqlite_db(population, number_of_products, 'cc')
    determine_surplus_for_all_products(population, number_of_products)

    print("\nHeap Status After Creating Few Objects : ")
    heap_status3 = heap.heap()
    print("Heap Size : ", heap_status3.size, " bytes\n")
    print(heap_status3)
    print("\nMemory Usage After Creation Of Objects : ", heap_status3.size - heap_status2.size, " bytes")
    perf_counter()

if __name__ == "__main__":
    analyze_heap()
    #analyze_sqlite_db('wc_products.txt')
    #load_more_data_to_sqlite_db('wc_products.txt')
