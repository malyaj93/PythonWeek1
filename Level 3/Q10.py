def count_customers_who_walked_away(N, S):
    occupied_computers = set()  # To track occupied computers
    customer_in_cafe = set()  # To track customers currently in the cafe
    walked_away_count = 0  # To track customers who walked away

    for customer in S:
        if customer not in customer_in_cafe:
            if len(occupied_computers) < N:  # If there is a free computer
                occupied_computers.add(customer)
                customer_in_cafe.add(customer)
            else:
                walked_away_count += 1
        else:
            occupied_computers.remove(customer)
            customer_in_cafe.remove(customer)

    return walked_away_count


N = int(input("Enter the number of computers: "))
S = input("Enter the sequence of arrivals and departures: ")
result = count_customers_who_walked_away(N, S)
print(f"Number of customers who walked away: {result}")
