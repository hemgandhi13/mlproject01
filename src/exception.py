import sys

def error_message_detail(error, error_detail: sys):
    # Get detailed information about the error
    _, _, exc_tb = error_detail.exc_info()  # Extract traceback info

    # Get the file name where the error occurred
    file_name = exc_tb.tb_frame.f_code.co_filename

    # Create a detailed error message
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message  # Return the error message


class CustomException(Exception):  # Inheriting from Exception
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)  # Initialize parent Exception class
        # Create a detailed error message using the function above
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message  # Return the error message when printed
