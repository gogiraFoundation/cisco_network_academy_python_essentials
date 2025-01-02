def fuel_converter(fuel=None, metrics=None):
    """
    A pair of functions converting between L/100km and mpg.
    """
    try:
        if fuel is not None and metrics is not None:
            if metrics == 'L/100km':
                # Convert from L/100km to mpg
                result = 235.214 / fuel
                return f"{fuel} L/100km is equal to {result:.2f} mpg."
            elif metrics == 'mpg':
                # Convert from mpg to L/100km
                result = 235.214 / fuel
                return f"{fuel} mpg is equal to {result:.2f} L/100km."
            else:
                return "Invalid metric. Use 'L/100km' or 'mpg'."
        else:
            return "Please provide both fuel and metrics."
    except Exception as e:
        return f"Error: {str(e)}"

# Example usage:
print(fuel_converter(10, 'L/100km'))  # Convert 10 L/100km to mpg
print(fuel_converter(30, 'mpg'))      # Convert 30 mpg to L/100km
