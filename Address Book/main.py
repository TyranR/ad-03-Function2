from contacts import Contact
from phonebook import PhoneBook


jhon = Contact('Jhon', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com', address='USA')
donald = Contact('Donald', 'Trump', '+712134267809', favorite=True, address='White House')
george = Contact('George', 'Bush', '+1232134267809', True, status='ExPresident')
bill = Contact('Bill', 'Clinton', '+7892134267809', instrument='Sax')
barack = Contact('Barack ', 'Obama', '+778934267809', born="Africa")

Mypb= PhoneBook('Mypb')
Mypb.add_new(jhon)
Mypb.add_new(donald)
Mypb.add_new(george)
Mypb.add_new(bill)
# Mypb.print_book()
# Mypb.remove('+71234567809')
# Mypb.print_book()
# Mypb.search_fav()
Mypb.search_by('Donald', 'Trump')
