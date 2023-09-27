import pickle


class ContactCard:
    name: str
    phone_number: str
    email: str


# Python data structures
# list, set, dict
# key / value

class AddressBook:
    data: dict[str, ContactCard] = {}
    filename: str

    def __init__(self, filename: str):
        self.filename = filename
        try:
            with open("contacts.bin", "rb") as f:
                self.data = pickle.load(f)
        except FileNotFoundError:
            pass

    def save(self):
        with open(self.filename, "wb") as f:
            pickle.dump(self.data, f)

    def add_contact(self, name: str) -> None:
        self.data[name] = ContactCard()

    def set_email(self, name: str, email: str) -> None:
        contact_card = self.data[name]
        contact_card.email = email

    def set_phone_number(self, name: str, phone: str) -> None:
        contact_card = self.data[name]
        contact_card.phone_number = phone

    def find(self, name_prefix: str) -> list[str]:
        result = []
        for name in self.data.keys():
            if name.startswith(name_prefix):
                result.append(name)
        return result


# calls AddressBook.__init__()
ab = AddressBook("contacts.bin")
print(ab.data)

ab.add_contact("fred")
ab.set_email("fred", "fred@gmail.com")
ab.set_phone_number("fred", "0521121333")

ab.add_contact("frank")
ab.add_contact("billy")
ab.add_contact("jane")

print(ab.find("fr"))
ab.save()

