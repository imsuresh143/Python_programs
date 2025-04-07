def check_password_validity(passwords):
    valid_password=[]
    for password in passwords:
        if 6<=len(password)<=12:
            lower=false
            upper=false
            digit=false
            special=false
            special_charaters="$#@"

            for char in password:
                if "a"<=char<="z":
                    lower=true
                elif"A"<=char<="Z":
                        upper=ture
                elif"0"<=char<="9":
                            digit=true
                elif char in special_characters:
                                special=true
        if lower and upper and digit and special:
                                    valid_password.append(password)
                                   
    return vaild_password
input_passwords=input("Enter passwords(comma Separted):")
password_list=[p.strip() for p in input_passwords.split(",")]
valid_passwords=check_password_vaildity(password_list)
print("vaild password:" +",".join(valid-passwords))
