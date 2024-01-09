def office_management(num_of_rooms):
    left_chairs = 0
    condition = True

    for room_number in range(info):
        data = input().split(' ')
        available_chairs = data[0]
        visitors = int(data[1])

        diff = abs(len(available_chairs) - visitors)

        if len(available_chairs) < visitors:
            condition = False
            print(f'{diff} more chairs needed in room {room_number + 1}')

        elif len(available_chairs) > visitors:
            left_chairs += diff

    if condition:
        print(f'Game On, {left_chairs} free chairs left')

info = int(input())
office_management(info)
