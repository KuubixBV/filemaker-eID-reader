from reader import eIDReader
import datetime
import os

# Create new instance of object and check if exists
eID = eIDReader("cherry")
if not eID:
    exit()

# Read card
if not eID.read_card():
    exit()

# Get eID contact object back from card
eID_contact = eID.get_last_read_eID_contact()

# Manipulate data for filemaker where needed

## Fix update timestamp to be in format d/m/y H:M:S - we will just overwrite the value in the class
updated = datetime.datetime.fromtimestamp(eID_contact.updated)
eID_contact.updated = updated.strftime('%d/%m/%Y %H:%M:%S')

## Fix validity begin timestamp to be in format d/m/y - we will just overwrite the value in the class
card_validity_begin = datetime.datetime.fromtimestamp(eID_contact.card_validity_begin)
eID_contact.card_validity_begin = card_validity_begin.strftime('%d/%m/%Y')

## Fix validity end timestamp to be in format d/m/y - we will just overwrite the value in the class
card_validity_end = datetime.datetime.fromtimestamp(eID_contact.card_validity_end)
eID_contact.card_validity_end = card_validity_end.strftime('%d/%m/%Y')

# Save eID contact as json
with open(os.path.join(os.path.expanduser('~'),'Documents/kuubix_eID/', "eID.json"), "w") as eID_file:
    eID_file.write(eID_contact.to_json())
