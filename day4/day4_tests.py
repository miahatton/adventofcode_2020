from day4_funcs import year_validity_check, height_validity_check, colour_validity_check, pid_check, all_checks
from typing import List

def test_year_validity():
    assert year_validity_check('2002', 'byr') == True, "2002 should be valid"
    assert year_validity_check('2003', 'byr') == False, "2003 should be invalid"
    
def test_height_validity():
    assert height_validity_check('60in') == True, "60in should be valid"
    assert height_validity_check('190in') == False, "190in should be invalid"
    assert height_validity_check('190cm') == True, "190cm should be valid"
    assert height_validity_check('190') == False, "190 should be invalid"
    
def test_colour_validity():
    assert colour_validity_check('#123abc', 'hcl') == True, "#123abc should be valid"
    assert colour_validity_check('#123abz', 'hcl') == False, "#123abz should be invalid"
    assert colour_validity_check('123abc', 'hcl') == False, "123abc should be invalid"
    assert colour_validity_check('brn', 'ecl') == True, "brn should be valid"
    assert colour_validity_check('wat', 'ecl') == False, "wat should be invalid"
    
def test_pid_validity():
    assert pid_check('000000001') == True, "000000001 should be valid"
    assert pid_check('0123456789') == False, "0123456789 should be invalid"
    
def test_passports(list_of_passports: List, valid: bool):
    for passport in list_of_passports:
        assert all_checks(passport) == valid, f"{passport} should be {'valid' if valid else 'invalid'}"