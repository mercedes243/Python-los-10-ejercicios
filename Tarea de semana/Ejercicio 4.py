phone_number = input("Please enter the phone number in the format +34-nnnnnnnnnn-xx: ")

parts = phone_number.split('-')


if len(parts) == 3 and parts[0] == '+34':
    
    main_number = parts[1]
    
    print("The phone number without prefix and extension is:", main_number)
else:
    print("The phone number is not in the correct format. Please use +34-nnnnnnnnnn-xx.")


