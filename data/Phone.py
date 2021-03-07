from abc import ABC, abstractmethod
import model.utils as utils
import string
from random import choice


numbers = string.digits
codes = ['903', '905', '906', '915', '916', '925', '926', '999']


class Phone(ABC):
    @abstractmethod
    def get_value(self) -> None:
        pass


class CompactCityPhone(Phone):
    def get_value(self) -> str:
        return f'7495{utils.get_random_word(numbers, 7)}'


class FullCityPhone(Phone):
    def get_value(self) -> str:
        return f'+7(49{choice("5689")}){utils.get_random_word(numbers, 3)}-{utils.get_random_word(numbers, 2)}-' \
               f'{utils.get_random_word(numbers, 2)}'


class FullMobilePhone(Phone):
    def get_value(self) -> str:
        return f'+7({choice(codes)}){utils.get_random_word(numbers, 3)}-{utils.get_random_word(numbers, 2)}-' \
               f'{utils.get_random_word(numbers, 2)}'


class CompactMobilePhone(Phone):
    def get_value(self) -> str:
        return f'7{choice(codes)}{utils.get_random_word(numbers, 7)}'


MOBILE_PHONE_TEMPLATES = [CompactMobilePhone(), FullMobilePhone()]
CITY_PHONE_TEMPLATES = [CompactCityPhone(), FullCityPhone()]
