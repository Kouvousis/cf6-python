def get_http_error(error_code):
    """
    Returns the HTTP error message corresponding to the given error code.
    
    Args:
        error_code (int): The HTTP error code.
    
    Returns:
        str: The corresponding error message.
    """
    errors = {
        200: "OK",
        400: "Bad Request",
        404: "Not Found"
    }
    return errors.get(error_code, "Unknown Error")


def main():
    error_code = 400
    print(get_http_error(error_code))

if __name__ == "__main__":
    main()