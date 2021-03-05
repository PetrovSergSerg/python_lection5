from random import randint, getrandbits
import string
import model.utils as utils
import datetime

alphabet = string.ascii_letters
numbers = string.digits


class Contact:
    def __init__(self, id=None, lastname=None, firstname=None, middlename=None, nickname=None,
                 title=None, company=None, address=None, phone_home=None, mobile=None, phone_work=None, fax=None,
                 email_main=None, email_secondary=None, email_other=None, homepage=None,
                 byear=None, bmonth=None, bday=None, ayear=None, amonth=None, aday=None,
                 address_secondary=None, phone_secondary=None, notes=None, emails=None, phones=None):
        self.id = id
        self.lastname = lastname
        self.firstname = firstname
        self.middlename = middlename
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.phone_home = phone_home
        self.mobile = mobile
        self.phone_work = phone_work
        self.fax = fax
        self.email_main = email_main
        self.email_secondary = email_secondary
        self.email_other = email_other
        self.homepage = homepage
        self.byear = byear
        self.bmonth = bmonth
        self.bday = bday
        self.ayear = ayear
        self.amonth = amonth
        self.aday = aday
        self.address_secondary = address_secondary
        self.phone_secondary = phone_secondary
        self.notes = notes
        self.emails = emails if emails is not None else self.calculate_emails()
        self.phones = phones if phones is not None else self.calculate_phones()

    def calculate_emails(self):
        # get list of emails for field in contact_list
        emails = [self.email_main, self.email_secondary, self.email_other]
        # filter this list by extracting all not-None elements
        emails = list(filter(lambda x: x is not None and x != "", emails))
        # and get string of list splitting all elements by "\n"
        return "" if len(emails) == 0 else "\n".join(emails)

    def calculate_phones(self):
        # get list of phones for field in contact_list
        phones = [self.phone_home, self.mobile, self.phone_work, self.phone_secondary]
        # filter this list by extracting all not-None elements
        phones = list(filter(lambda x: x is not None and x != "", phones))
        # and get string of list splitting all elements by "\n"
        return "" if len(phones) == 0 else "\n".join(phones)

    def set_empty_parameters(self):
        for name, value in self.__dict__.items():
            if name in ['bday', 'bmonth', 'aday', 'amonth']:
                setattr(self, name, '-')
            else:
                setattr(self, name, '')
        self.id = None

        return self

    def set_random_parameters_to_random_value(self):
        # getrandbits(1) returns 0 or 1 with 50% probability
        # with 50% probability generate random word on alphabet with random length
        # and with probability 50% returns EMPTY_STRING
        if bool(getrandbits(1)):
            self.lastname = '' if bool(getrandbits(1)) else utils.get_random_word(alphabet, randint(3, 10))
        if bool(getrandbits(1)):
            self.firstname = '' if bool(getrandbits(1)) else utils.get_random_word(alphabet, randint(3, 10))
        if bool(getrandbits(1)):
            self.middlename = '' if bool(getrandbits(1)) else utils.get_random_word(alphabet, randint(3, 10))
        if bool(getrandbits(1)):
            self.nickname = '' if bool(getrandbits(1)) else utils.get_random_word(alphabet, randint(3, 10))

        # getrandbits(1) returns 0 or 1 with 50% probability
        # with 50% probability generate random word on alphabet with random length
        # and with probability 50% returns EMPTY_STRING
        if bool(getrandbits(1)):
            self.title = '' if bool(getrandbits(1)) else utils.get_random_word(alphabet, randint(3, 10))
        if bool(getrandbits(1)):
            self.company = '' if bool(getrandbits(1)) else utils.get_random_word(alphabet, randint(3, 10))
        if bool(getrandbits(1)):
            self.address = '' if bool(getrandbits(1)) else utils.get_random_word(alphabet + ' ', randint(10, 20))

        # 30% probability to be empty value
        if bool(getrandbits(1)):
            self.phone_home = '' if randint(0, 2) < 1 else '+7495' + utils.get_random_word(numbers, 7)
        # 10% probability to be empty value
        if bool(getrandbits(1)):
            self.mobile = '' if randint(0, 9) < 1 else '+79' + utils.get_random_word(numbers, 9)
        # 50% probability to be empty value
        if bool(getrandbits(1)):
            self.phone_work = '' if bool(getrandbits(1)) else '+79' + utils.get_random_word(numbers, 9)
        # 10% probability to be empty value
        if bool(getrandbits(1)):
            self.fax = '' if randint(0, 9) < 1 else '+7495' + utils.get_random_word(numbers, 7)

        # randint(0, 4) < 1 = 20%; randint(0, 4) < 4 = 80%
        # with some probability generate random word on alphabet with random length
        if bool(getrandbits(1)):
            self.email_main = '' if randint(0, 4) < 1 else utils.get_random_email(alphabet)
        if bool(getrandbits(1)):
            self.email_secondary = '' if randint(0, 4) < 4 else utils.get_random_email(alphabet)
        if bool(getrandbits(1)):
            self.email_other = '' if randint(0, 4) < 4 else utils.get_random_email(alphabet)
        if bool(getrandbits(1)):
            self.homepage = '' if bool(getrandbits(1)) \
                else 'http://' + utils.get_random_word(alphabet, randint(3, 10)) + '.com'

        start = datetime.date(1980, 1, 1)
        end = datetime.date(2000, 12, 31)
        bd = utils.get_random_date(start, end)  # get random date between given dates
        if bool(getrandbits(1)):  # 50% probability set birthdate
            self.byear = bd.strftime('%Y')  # get year from this date
            self.bmonth = bd.strftime('%B')  # get month in format April, January, ...
            self.bday = str(int(bd.strftime('%d')))  # because %d is date with leading 0: 01, 02, 03, ... 11, 12, ...

        if bool(getrandbits(1)):  # 50% probability to generate anniversary date
            anniversary = utils.get_random_date(bd, datetime.date.today())  # random date from BD to TODAY
            self.ayear = anniversary.strftime('%Y')
            self.amonth = anniversary.strftime('%B')
            self.aday = str(int(anniversary.strftime('%d')))

        # randint(0, 2) < 2 = 66%; getrandbits(1) returns 0 or 1 with 50% probability
        # with some probability generate random word on alphabet with random length
        if bool(getrandbits(1)):
            self.address_secondary = '' if randint(0, 2) < 2 else utils.get_random_word(alphabet + ' ', randint(10, 20))
        if bool(getrandbits(1)):
            self.phone_secondary = '' if randint(0, 2) < 2 else '+7495' + utils.get_random_word(numbers, 7)
        if bool(getrandbits(1)):
            self.notes = '' if bool(getrandbits(1)) else utils.get_random_word(alphabet + ' ', randint(10, 20))
        self.emails = self.calculate_emails()
        self.phones = self.calculate_phones()

        return self

    def set_all_parameters_to_random_value(self):
        self.lastname = utils.get_random_word(alphabet, randint(3, 10))
        self.firstname = utils.get_random_word(alphabet, randint(3, 10))
        self.middlename = utils.get_random_word(alphabet, randint(3, 10))
        self.nickname = utils.get_random_word(alphabet, randint(3, 10))

        self.title = utils.get_random_word(alphabet, randint(3, 10))
        self.company = utils.get_random_word(alphabet, randint(3, 10))
        self.address = utils.get_random_word(alphabet + ' ', randint(10, 20))

        self.phone_home = '+7495' + utils.get_random_word(numbers, 7)
        self.mobile = '+79' + utils.get_random_word(numbers, 9)
        self.phone_work = '+79' + utils.get_random_word(numbers, 9)
        self.fax = '+7495' + utils.get_random_word(numbers, 7)

        self.email_main = utils.get_random_email(alphabet)
        self.email_secondary = utils.get_random_email(alphabet)
        self.email_other = utils.get_random_email(alphabet)
        self.homepage = 'http://' + utils.get_random_word(alphabet, randint(3, 10)) + '.com'

        start = datetime.date(1980, 1, 1)
        end = datetime.date(2000, 12, 31)
        bd = utils.get_random_date(start, end)  # get random date between given dates
        self.byear = bd.strftime('%Y')  # get year from this date
        self.bmonth = bd.strftime('%B')  # get month in format April, January, ...
        self.bday = str(int(bd.strftime('%d')))  # because %d is date with leading 0: 01, 02, 03, ... 11, 12, ...

        anniversary = utils.get_random_date(bd, datetime.date.today())  # random date from BD to TODAY
        self.ayear = anniversary.strftime('%Y')
        self.amonth = anniversary.strftime('%B')
        self.aday = str(int(anniversary.strftime('%d')))

        self.address_secondary = '' if randint(0, 2) < 2 else utils.get_random_word(alphabet + ' ', randint(10, 20))
        self.phone_secondary = '' if randint(0, 2) < 2 else '+7495' + utils.get_random_word(numbers, 7)
        self.notes = '' if bool(getrandbits(1)) else utils.get_random_word(alphabet + ' ', randint(10, 20))

        self.emails = self.calculate_emails()
        self.phones = self.calculate_phones()

        return self

    def __eq__(self, other):
        return (self.id is None
                or other.id is None
                or self.id == other.id) \
               and self.lastname == other.lastname \
               and self.firstname == other.firstname \
               and self.address == other.address \
               and self.emails == other.emails \
               and self.phones == other.phones

    def __repr__(self):
        fio = [self.lastname, self.firstname]
        return f'Contact({self.id}, FIO=\"{" ".join(filter(lambda x: x != "", fio))}\", ' \
               f'ADDRESS=\"{self.address}\", EMAILS=\"{self.emails}\", PHONES=\"{self.phones}\")'

    def __lt__(self, other):
        # None >> any integer
        # self.id = None => return False (left bigger)
        # other.id is None => return True (right is bigger)
        # else compare int(self.id) <> int(other.id), because type(Group.id) = str, but it's a number!
        return self.id is not None \
               and (other.id is None
                    or int(self.id) < int(other.id))
