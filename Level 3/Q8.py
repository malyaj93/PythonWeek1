def parse_encoded_string(encoded_str):
    # Split the string by '0' and filter out empty values
    parts = list(filter(None, encoded_str.split('0')))

    # Assuming the first part is the first name, second is the last name, and third is the ID
    if len(parts) != 3:
        return "Invalid input format."

    first_name = parts[0]
    last_name = parts[1]
    id_value = parts[2]

    # Construct the dictionary with parsed values
    result = {
        'first_name': first_name,
        'last_name': last_name,
        'id': id_value
    }

    return result

encoded_string = input("Enter the encoded string: ")
parsed_result = parse_encoded_string(encoded_string)
print("Parsed Dictionary:", parsed_result)
