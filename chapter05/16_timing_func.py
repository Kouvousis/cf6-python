import time

def get_time(n):
    start_time = time.perf_counter()
    # make some calculations
    result = sum(range(n))
    end_time = time.perf_counter()
    
    print(f"My function took {end_time - start_time: .6f} seconds to run")
    return result

def main():
    print(get_time(1_000_000))

if __name__ == "__main__":
    main()