def main():
    store_a_products = {"Apples", "Bananas", "Cherries", "Elderberries"}
    store_b_products = {"Bananas", "Cherries", "Figs", "Grapes"}
    
    print("Original store a:", store_a_products)
    print("Original store b:", store_b_products)
    
    # intersection
    # common_products = store_a_products.intersection(store_b_products)
    common_products = store_a_products & store_b_products
    print("Common products:", common_products)    
    
    # union
    # all_products = store_a_products | store_b_products
    all_products = store_a_products.union(store_b_products)
    print("All products:", all_products)
    
    # find the products in Store A but not in Store b
    # store_a_exclusive = store_a_products - store_b_products
    store_a_exclusive = store_a_products.difference(store_b_products)
    print("Store A exclusive products", store_a_exclusive)
    
    # symmetric difference
    unique_either_products = store_a_products ^ store_b_products
    print("Products in A or B but not in A and B", unique_either_products)

if __name__ == "__main__":
    main()