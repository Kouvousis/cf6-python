import logging

def main():
    log_file = 'cf6.log'
    
    # create a file handler for logging to a file
    file_handler = logging.FileHandler(log_file, mode='a')
    
    # create a list of handler
    handlers = [file_handler]
    
    # create a logger
    logger = logging.getLogger('search-app')
    
    # configuration
    logging.basicConfig(
        handlers=handlers,
        level=logging.INFO,
        format="%(asctime)s:%(levelname)s%(name)s%(message)s"
    )
    
    nums = [10, 20, 30, 40, 50]
    
    try:
        index = nums.index(3000)
        print("Found")
        print(index)
    except ValueError as e:
        # log an error
        logger.error(f"Error occurred: {e}", exc_info=True)
        
    
    

if __name__ == "__main__":
    main()