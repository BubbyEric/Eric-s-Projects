#Eric Pham, 8/7/24, ITSS 4381
def main():
    print("HELLO, WELCOME TO BUBBY'S RENTAL SCOOTER SHOP!!!")
    price_list = ['Hourly: $7', 
                  'Daily: $25',
                  'Weekly: $70']
    print(f'Rental options: {price_list}')
                  

    try:
        total_scooters = 7
        total_rented_scooters = 0
        rentals = {}

        while True:
            remaining_scooters = total_scooters - total_rented_scooters

            if total_rented_scooters >= total_scooters:
                print('7/7 SCOOTERS ALL RENTED OUT! PLEASE COME AGAIN ANOTHER TIME, THANK YOU!!! :D')
            
            action = input('Enter "rent" to rent scooters, "return" to return scooters, or "404" to cancel: ').lower()

            if action == '404':
                print('<Ending transaction...thank you for your time.>')
                break

            if action == 'rent':
                if total_rented_scooters >= total_scooters:
                    print('Currently, all scooters are rented out. Please return some scooters before renting more.')
                    continue
                
                name = input('To begin the rental process, enter your name: ')
                
                while True:
                    scooters_to_rent = int(input(f'Awesome! Please enter how many scooters you would like to rent (remaining scooters: {remaining_scooters}): '))
                    
                    if scooters_to_rent == 404:
                        print('<Ending transaction...thank you for your time.>')
                        return  
                    
                    if scooters_to_rent > remaining_scooters:
                        print(f'**Error, insufficient number of scooters available. Only {remaining_scooters} scooter(s) left. Please try again.**')
                        continue  
                    
                    if scooters_to_rent <= 0:
                        print('*Error, cannot rent 0 or negative scooters. Please try again*')
                        continue
                    
                    rental_period = input("Confirmed, please enter 'hour', 'day', or 'week' as your preferred rental period: ").lower()
                    
                    if rental_period == 'hour':
                        hours_rented = float(input('Great! Almost done, now please enter how many hours you would like to rent your scooter: '))
                        
                        if hours_rented == 404:
                            print('<Ending transaction...thank you for your time.>')
                            return  
                        
                        if hours_rented < 24:
                            total_cost = hours_rented * 7 * scooters_to_rent
                            discount_message = ''
                            if scooters_to_rent >= 3 and scooters_to_rent <= 5:
                                total_cost *= 0.7
                                discount_message = '30% DISCOUNT APPLIED'
                            print(f'Total: ${total_cost:.2f}. Please return the scooter on time to avoid a $5 late fee. Thank you and enjoy!')
                            receipt = [
                                f'NAME: {name}',
                                f'NUMBER OF SCOOTERS: {scooters_to_rent}',
                                f'RENTAL PERIOD: Hourly',
                                f'HOURS RENTED: {hours_rented}',
                                f'{discount_message}',
                                f'TOTAL: ${total_cost:.2f}'
                            ]
                            print('RECEIPT:')
                            for line in receipt:
                                print(line)
                            
                            # Record the rental
                            rentals[name] = {
                                'scooters': scooters_to_rent,
                                'period': 'hour',
                                'duration': hours_rented
                            }
                            
                            total_rented_scooters += scooters_to_rent
                            break
                    
                        else:
                            print('*Invalid input, please try again*')
                    
                    elif rental_period == 'day':
                        days_rented = float(input('Great! Almost done, now please enter how many days you would like to rent your scooter: '))
                        
                        if days_rented == 404:
                            print('<Ending transaction...thank you for your time.>')
                            return  
                        
                        if days_rented < 7:
                            total_cost = days_rented * 25 * scooters_to_rent
                            discount_message = ''
                            if scooters_to_rent >= 3 and scooters_to_rent <= 5:
                                total_cost *= 0.7
                                discount_message = '30% DISCOUNT APPLIED'
                            print(f'Total: ${total_cost:.2f}. Please return the scooter on time to avoid a $5 late fee. Thank you and enjoy!')
                            receipt = [
                                f'NAME: {name}',
                                f'NUMBER OF SCOOTERS: {scooters_to_rent}',
                                f'RENTAL PERIOD: Daily',
                                f'DAYS RENTED: {days_rented}',
                                f'{discount_message}',
                                f'TOTAL: ${total_cost:.2f}'
                            ]
                            print('RECEIPT:')
                            for line in receipt:
                                print(line)
                            
                            # Record the rental
                            rentals[name] = {
                                'scooters': scooters_to_rent,
                                'period': 'day',
                                'duration': days_rented
                            }
                            
                            total_rented_scooters += scooters_to_rent
                            break
                    
                        else:
                            print('*Invalid input, please try again*')
                    
                    elif rental_period == 'week':
                        weeks_rented = float(input('Great! Almost done, now please enter how many weeks you would like to rent your scooter: '))
                        
                        if weeks_rented == 404:
                            print('<Ending transaction...thank you for your time.>')
                            return
                        
                        if weeks_rented < 24:
                            total_cost = weeks_rented * 70 * scooters_to_rent
                            discount_message = ''
                            if scooters_to_rent >= 3 and scooters_to_rent <= 5:
                                total_cost *= 0.7
                                discount_message = '30% DISCOUNT APPLIED'
                            print(f'Total: ${total_cost:.2f}. Please return the scooter on time to avoid a $5 late fee. Thank you and enjoy!')
                            receipt = [
                                f'NAME: {name}',
                                f'NUMBER OF SCOOTERS: {scooters_to_rent}',
                                f'RENTAL PERIOD: Weekly',
                                f'WEEKS RENTED: {weeks_rented}',
                                f'{discount_message}',
                                f'TOTAL: ${total_cost:.2f}'
                            ]
                            print('RECEIPT:')
                            for line in receipt:
                                print(line)
                            
                            # Record the rental
                            rentals[name] = {
                                'scooters': scooters_to_rent,
                                'period': 'week',
                                'duration': weeks_rented
                            }
                            
                            total_rented_scooters += scooters_to_rent
                            break
                    
                        else:
                            print('*Invalid input, please try again*')
                    
                    elif rental_period == '404':
                        print('<Ending transaction...thank you for your time.>')
                        return
                    
                    else:
                        print('***Invalid rental period, please try again***')

            elif action == 'return':
                return_name = input('Enter the name under which the scooters were rented: ')
                
                if return_name in rentals:
                    return_scooters = int(input(f'How many scooters would you like to return (currently rented: {rentals[return_name]["scooters"]}): '))
                    
                    if return_scooters == 404:
                        print('<Ending transaction...thank you for your time.>')
                        return
                    
                    if return_scooters <= 0 or return_scooters > rentals[return_name]['scooters']:
                        print('*Error, invalid number of scooters to return. Please try again.*')
                        continue
                    
                    return_period = rentals[return_name]['period']
                    return_duration = float(input(f'How long did you use the scooters for? Enter in {return_period}: '))
                    
                    if return_duration == 404:
                        print('<Ending transaction...thank you for your time.>')
                        return
                    
                    original_duration = rentals[return_name]['duration']
                    
                    if return_duration > original_duration:
                        late_fee = (return_duration - original_duration) * 5
                        print(f'Late fee of ${late_fee:.2f} applied.')
                    else:
                        late_fee = 0
                    
                    if return_period == 'hour':
                        total_cost = return_duration * 7 * return_scooters
                    elif return_period == 'day':
                        total_cost = return_duration * 25 * return_scooters
                    elif return_period == 'week':
                        total_cost = return_duration * 70 * return_scooters
                    
                    total_cost += late_fee
                    
                    receipt = [
                        f'NAME: {return_name}',
                        f'NUMBER OF SCOOTERS RETURNED: {return_scooters}',
                        f'RENTAL PERIOD: {return_period.capitalize()}',
                        f'DURATION RETURNED: {return_duration}',
                        f'Late Fee: ${late_fee:.2f}',
                        f'TOTAL COST: ${total_cost:.2f}'
                    ]
                    
                    print('RETURN RECEIPT:')
                    for line in receipt:
                        print(line)
                    
                    # Update the rented scooters and remove the rental record
                    total_rented_scooters -= return_scooters
                    del rentals[return_name]
                    
                else:
                    print('*Error, no rental record found under that name. Please try again.*')
            
            else:
                print('***Invalid action. Please enter "rent" or "return"***')

    except Exception as e:
        print(f'****ERROR, unexpected glitch: {e}****')
        print('Contact support services at 123-456-7890')

if __name__ == "__main__":
    main()
