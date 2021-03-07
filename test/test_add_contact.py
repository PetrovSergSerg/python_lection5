import pytest
from model.contact import Contact
from model.utils import random_string, get_random_word
from random import getrandbits, randint, choice
import data.constants as constant

testdata = [
    Contact(lastname="" if private and bool(getrandbits(1)) else random_string("lastname", 15),
            firstname="" if private and bool(getrandbits(1)) else random_string("firstname", 10),
            middlename="" if private and bool(getrandbits(1)) else random_string("middlename", 15),
            nickname="" if private and bool(getrandbits(1)) else random_string("nickname", 10),
            title="" if private and bool(getrandbits(1)) else random_string("title", 20),
            company="" if private and bool(getrandbits(1)) else random_string("company", 30),
            address="" if private and bool(getrandbits(1)) else random_string("address", 50),
            phone_home="" if phones and bool(getrandbits(1)) else random_string("phone_home", 15),
            mobile="" if phones and bool(getrandbits(1)) else random_string("mobile", 15),
            phone_work="" if phones and bool(getrandbits(1)) else random_string("phone_work", 15),
            fax="" if phones and bool(getrandbits(1)) else random_string("fax", 15),
            email_main="" if emails and bool(getrandbits(1)) else random_string("email_main", 15),
            email_secondary="" if emails and bool(getrandbits(1)) else random_string("email_secondary", 15),
            email_other="" if emails and bool(getrandbits(1)) else random_string("email_other", 15),
            homepage="" if emails and bool(getrandbits(1)) else random_string("homepage", 15),
            byear="" if emails and bool(getrandbits(1)) else get_random_word(constant.SYMBOLS, randint(1, 4)),
            bmonth="-" if emails and bool(getrandbits(1)) else choice(constant.MONTHS),
            bday="" if emails and bool(getrandbits(1)) else str(randint(1, 31)),
            ayear="" if emails and bool(getrandbits(1)) else get_random_word(constant.SYMBOLS, randint(1, 4)),
            amonth="-" if emails and bool(getrandbits(1)) else choice(constant.MONTHS),
            aday="" if emails and bool(getrandbits(1)) else str(randint(1, 31)),
            address_secondary="" if secondary and bool(getrandbits(1)) else random_string("address_secondary", 15),
            phone_secondary="" if secondary and bool(getrandbits(1)) else random_string("phone_secondary", 15),
            notes="" if secondary and bool(getrandbits(1)) else random_string("notes", 15))
    for private in [True, False]
    for phones in [True, False]
    for emails in [True, False]
    for secondary in [True, False]
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(c) for c in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)

    # new list is longer, because we added 1 element
    assert app.contact.count() == len(old_contacts) + 1

    # if new list length is correct, then we can compare lists.
    # so we can get new list
    new_contacts = app.contact.get_contact_list()

    # make sure that all elements of OLD list are in NEW list
    assert all(elem in new_contacts for elem in old_contacts)

    # built expected list for equalizing NEW and EXPECTED
    # expected list = old_list + new contact. And sort()
    # sort() will use method __lt__, which was overridden
    old_contacts.append(contact)
    assert sorted(new_contacts) == sorted(old_contacts)
