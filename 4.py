import string

from aoc import get_input


class Passport:
    def __init__(self, record):
        record = dict(kv.split(':') for kv in record.split())
        self.record = record

        self.byr = int(record['byr']) if 'byr' in record else None
        self.iyr = int(record['iyr']) if 'iyr' in record else None
        self.eyr = int(record['eyr']) if 'eyr' in record else None

        self.hgt = None
        self.hgt_unit = None
        if 'hgt' in record:
            if record['hgt'].endswith(('cm', 'in')):
                self.hgt_unit = record['hgt'][-2:]

                measurement = record['hgt'][:-2]
                if measurement.isnumeric():
                    self.hgt = int(measurement)
            elif record['hgt'].isnumeric():
                self.hgt = record['hgt']

        self.hcl = record['hcl'] if 'hcl' in record else None
        self.ecl = record['ecl'] if 'ecl' in record else None

        self.pid = record['pid'] if 'pid' in record else None
        self.cid = record['cid'] if 'cid' in record else None

    @staticmethod
    def cm_to_in(value):
        return value / 2.54

    @staticmethod
    def in_to_cm(value):
        return value * 2.54

    def has_required_fields(self):
        return all(field in self.record for field in ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'))

    def is_valid(self):
        try:
            assert self.has_required_fields()

            assert 1920 <= self.byr <= 2002
            assert 2010 <= self.iyr <= 2020
            assert 2020 <= self.eyr <= 2030

            # height
            assert self.hgt_unit in ('cm', 'in')
            if self.hgt_unit == 'cm':
                assert 150 <= self.hgt <= 193
            elif self.hgt_unit == 'in':
                assert 59 <= self.hgt <= 76

            # hair color
            assert len(self.hcl) == 7
            assert self.hcl.startswith('#')
            assert all(c in string.hexdigits for c in self.hcl[1:])

            assert self.ecl in 'amb blu brn gry grn hzl oth'.split()

            assert len(self.pid) == 9
            assert self.pid.isnumeric()

            return True
        except AssertionError:
            return False


batchfile = '\n'.join(get_input(day=4)).split('\n\n')

# 4-1
print(sum(Passport(entry).has_required_fields() for entry in batchfile))

# 4-2
print(sum(Passport(entry).is_valid() for entry in batchfile))

# tests:
invalid_examples = """eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007"""
assert not all(Passport(entry).is_valid() for entry in invalid_examples.split('\n\n'))

valid_examples = """pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"""
assert all(Passport(entry).is_valid() for entry in valid_examples.split('\n\n'))
