def main():
    inventory = {}
    while True:
        try:
            user = int(input('Add[1], Remove[2], View[3], Exit[4]'))
            if user not in [1, 2, 3, 4]:
                print('Input should be a positive integer in range 1-4')
                continue
        except ValueError:
            print('Input should be positive integer')
            continue
        if user == 1:
            item_name = input('Item name:')
            try:
                quantity = int(input('Quantity to add:'))
                if quantity <= 0:
                    print('Quantity should be a positive integer')
                    continue
            except ValueError:
                print('Quantity should be a integer')
                continue
            if item_name in inventory:
                inventory[item_name] += quantity
            else:
                inventory[item_name] = quantity
            print(f'Added {quantity} of {item_name}')
        elif user == 2:
            item_name = input('Item name:')
            if item_name in inventory:
                try:
                    quantity = int(input('Quantity to remove:'))
                    if quantity <= 0:
                        print('Quantity should be a positive integer')
                        continue
                except ValueError:
                    print('Input should be a positive integer')
                    continue
                if quantity >= inventory[item_name]:
                    del inventory[item_name]
                    print(f'{item_name} removed')
                else:
                    inventory[item_name] -= quantity
                    print(f'Removed {quantity} from {item_name}')
            else:
                print(f'No {item_name} in inventory')
        elif user == 3:
            if not inventory:
                print('Inventory is empty')
            else:
                for item, quantity in inventory.items():
                    print(item, quantity)
        elif user == 4:
            print('Exiting the program.')
            break
        else:
            print('Input should be positive integer in range 1-4')


if __name__ == '__main__':
    main()
