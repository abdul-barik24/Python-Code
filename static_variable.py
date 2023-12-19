#static variable | Hall Room Booking
class hall_room:
    total_seat = 1000       #static variable
    booking_seat = 0
    available_seat = 1000

    def __init__(self, name, mobile, city):
        self.name = name
        self.mobile = mobile
        self.city = city
        hall_room.booking_seat += 1
        hall_room.available_seat -= 1

    def participant_info(self):
        print(f'Name: {self.name}, mobile: {self.mobile} and city: {self.city}')

p1 = hall_room('Mita', '+88 01712 XXX XXX', 'Dhaka')
p2 = hall_room('Raju', '+88 01712 000 XXX', 'Sherpur')
p3 = hall_room('Mina', '+88 01712 XXX 000', 'Sylhet')
p4 = hall_room('Hena', '+88 01712 XXX 000', 'Sylhet')

p1.participant_info()
p2.participant_info()
p3.participant_info()
p4.participant_info()

print('------------------------------')
print('Total Seats:', hall_room.total_seat)
print('Total Booking:', hall_room.booking_seat)
print('Total Available:', hall_room.available_seat)
