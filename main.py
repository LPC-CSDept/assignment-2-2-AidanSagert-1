def main():
    """
    ##################################################
    # Comlete your code here
    Use the same variables: celsius fahrenheit 
    ##################################################
    """
    celsius = int(input("Enter a temperature in celsius"))
    fahrenheit = 9/5 * celsius + 32
    print("Fahrenheit: {:.2f}".format(fahrenheit))

    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return celsius, fahrenheit
if __name__ == '__main__':
    main()
