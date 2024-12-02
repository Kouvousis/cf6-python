from typing import List, Tuple

def get_results(products: List[Tuple[str, int]], **kwargs) -> List[Tuple[str, int]]:
    """
    Filters a list of products based on given keyword arguments.
    Each keyword responds to a product attribute.
    
    Parameters:
        product(List[Tuple(str, int)]): A list of tuples where each tuple contains a brand and a price.
        **kwargs: Arbitrary keyword arguments (brand, price)
        
    Returns:
        List[Tuple(str, int)]: A list tuples that 'match' the filtering criteria.
    """
    results = [
        (brand, price) for brand, price in products if kwargs.get('brand') == brand and kwargs.get('price') == price
    ]
    return results
    

def main():
    products = [("Lenovo", 100), ("Lenovo", 40), ("IBM", 100)]
    criteria = {
        "brand": "Lenovo",
        "price": 100
    }
    
    print(get_results(products, **criteria))

if __name__ == "__main__":
    main()