from model.contact import Contact


def test_add_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact().set_empty_parameters()  # generate empty contact
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
    old_contacts.sort()
    new_contacts.sort()
    assert new_contacts == old_contacts


def test_add_handled_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(lastname='aaa', firstname='bbb', middlename='ccc', nickname='ddd', title='kkk',
                      company='lll', address='mmm', phone_home='111', mobile='222', phone_work='333', fax='444',
                      email_main='a@a.ru', email_secondary='b@b.ru', email_other='c@c.ru', homepage='http://',
                      byear='1994', bmonth='April', bday='15', ayear='2003', amonth='September', aday='4',
                      address_secondary='xxx', phone_secondary='777', notes='zzz')
    app.contact.create(contact)

    # new list is longer, because we added 1 element
    assert app.contact.count() == len(old_contacts) + 1

    # if new list length is correct, then we can compare lists.
    # so we can get new list
    new_contacts = app.contact.get_contact_list()

    # make sure that all elements of OLD list are in NEW list
    # for elem in old_contacts:
    #     assert elem in new_contacts
    assert all(elem in new_contacts for elem in old_contacts)

    # built expected list for equalizing NEW and EXPECTED
    # expected list = old_list + new contact. And sort()
    # sort() will use method __lt__, which was overridden
    old_contacts.append(contact)
    old_contacts.sort()
    new_contacts.sort()
    assert new_contacts == old_contacts


def test_add_random_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact().set_all_parameters_to_random_value()  # generate fully random contact
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
    old_contacts.sort()
    new_contacts.sort()
    assert new_contacts == old_contacts
