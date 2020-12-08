import re

print('Day 4, puzzle 2 - passport processing with data validation')

# input_file = "example_set_2"
input_file = "input"

# expected passport fields
# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)

required_fields={'byr','iyr','eyr','hgt','hcl','ecl','pid'}
optional_fields={'cid'}
valid_passports=0
invalid_passports=0
failed_checks=0

invalid_byr=0
invalid_eyr=0
invalid_iyr=0
invalid_hcl=0
invalid_hgt=0
invalid_ecl=0
invalid_pid=0
# invalid_hgt=0

def check_passport_fields(fields):
    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    global invalid_byr
    byr = fields['byr']
    # print('Birth Year:',byr)
    if len(re.findall('[0-9]+', byr)[0]) != 4:
        invalid_byr += 1
        return False
    if int(byr) < 1920 or int(byr) > 2002:
        invalid_byr += 1
        return False

    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    global invalid_iyr
    iyr = fields['iyr']
    # print('Issue Year:',iyr)
    if len(re.findall('[0-9]+', iyr)[0]) != 4:
        invalid_iyr += 1
        return False
    if int(iyr) < 2010 or int(iyr) > 2020:
        invalid_iyr += 1
        return False

    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    global invalid_eyr
    eyr = fields['eyr']
    # print('Expiration Year:',eyr)
    if len(re.findall('[0-9]+', eyr)[0]) != 4:
        invalid_eyr += 1
        return False
    if int(eyr) < 2020 or int(eyr) > 2030:
        invalid_eyr += 1
        return False

    # hgt (Height) - a number followed by either cm or in:
    # If cm, the number must be at least 150 and at most 193.
    # If in, the number must be at least 59 and at most 76.
    global invalid_hgt
    hgt = fields['hgt']
    if hgt[-2:] not in {'cm','in'}:
        # print(f'invalid height: {hgt}')
        invalid_hgt += 1
        return False
    if hgt[-2:] == 'cm':
        if len(hgt) != 5:
            invalid_hgt += 1
            # print(f'invalid height: {hgt}')
            return False
        if int(hgt[:3]) < 150 or int(hgt[:3]) > 193:
            # print(f'invalid height: {hgt}')
            invalid_hgt += 1
            return False
    if hgt[-2:] == 'in':
        if len(hgt) != 4:
            invalid_hgt += 1
            # print(f'invalid height: {hgt}')
            return False
        if int(hgt[:2]) < 59 or int(hgt[:2]) > 76:
            # print(f'invalid height: {hgt}')
            invalid_hgt += 1
            return False

    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    global invalid_hcl
    hcl = fields['hcl']
    # print('Hair Colour:',hcl)
    if hcl[0] != '#':
        invalid_hcl += 1
        # print(f'invalid hair color: {hcl}')
        return False

    if len(re.findall('[0-9,a-f]+', hcl)[0]) != 6:
        invalid_hcl += 1
        # print(f'invalid hair color: {hcl}')
        return False

    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    global invalid_ecl
    ecl = fields['ecl']
    # print('Eye Colour:',ecl)
    if ecl not in {'amb','blu','brn','gry','grn','hzl','oth'}:
        invalid_ecl += 1
        return False

    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    global invalid_pid
    pid = fields['pid']
    # print('Passport ID:',pid)
    if len(re.findall('[0-9]+', pid)[0]) != 9:
        invalid_pid += 1
        return False

    return True


new_passport = True
fields={}
with open(input_file,"r") as f:
    lines = f.readlines()
    last = lines[-1]
    for line in lines:
        if len(line) == 1:
            new_passport = True
        else:
            new_passport = False
            for i in line.split():
                k = i.split(':')[0]
                v = i.split(':')[1]
                fields[k] = v

        if (line is last) or new_passport:
            missing = required_fields.difference(fields)
            if len(missing) == 0 or (len(missing) == 1 and len(missing.difference(optional_fields)) == 0):
                if check_passport_fields(fields):
                    valid_passports += 1
                else:
                    failed_checks += 1
                    invalid_passports += 1
            else:
                invalid_passports += 1
            fields={}

print(f'valid passports: {valid_passports}')
print(f'valid passports with failed checks: {failed_checks}')
print(f'invalid passports: {invalid_passports}')
print('invalid birth year:',invalid_byr)
print('invalid issue year:',invalid_iyr)
print('invalid expiry year:',invalid_eyr)
print('invalid passport id:',invalid_pid)
print('invalid height:',invalid_hgt)
print('invalid hair color:',invalid_hcl)
print('invalid eye color:',invalid_ecl)
print('invalid passport id:',invalid_pid)
