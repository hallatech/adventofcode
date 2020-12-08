print('Day 4, puzzle 1 - passport processing?')

# input_file = "example_set"
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
                valid_passports += 1
            else:
                invalid_passports += 1
            fields={}

print(f'valid passports: {valid_passports}')
print(f'invalid passports: {invalid_passports}')
