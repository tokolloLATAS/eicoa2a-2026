def calc_resistance(voltage, current):
    """
    Calculate the resistance using Ohm's Law.
    
    Args:
        voltage (float): The voltage across the resistor.
        current (float): The current through the resistor.
    
    Returns:
        float: The resistance of the resistor
    Notes:
        The function raises a ZeroDivisionError if current is 0.
    """
    return voltage / current
