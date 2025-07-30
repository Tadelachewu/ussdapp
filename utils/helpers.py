def is_valid_amount(amount_str):
    return amount_str.isdigit() and 0 < int(amount_str) <= 10000
