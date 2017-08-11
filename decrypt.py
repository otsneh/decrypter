import sys

# sample message: N30q"r pu n2q3 2q: O0w2yy0 5086. X6 0w7 xl 3vx26 )k0x0q 1prq u0sz67 vps ry09 vpqr276? N6"s6 yvvz2w4 5vs rvx6n36s6 qv uvrq pu vps (y08z 0rr6r 5vs q36 w243q? Rv: p3: 90w4 90w4: rz66q rz66q: w2440? !prq 0 8vpuy6 v5 u2xur: wv 3vr?

CHAR_FREQUENCY = "etaoinsrhldcumfgpywb,.vk-\"_'x)(;0j1q=2:z/*!?$35>{}49[]867\\+|&<%@#^`~"
CHARS_TO_IGNORE = " "

def decrypt(encrypted_message):
    decrypted_message = _decrypt_message(encrypted_message, CHAR_FREQUENCY)
    return decrypted_message

def _perform_decryption(encrypted_message, decrypted_char_by_encrypted_char):
    decrypted_message = ''
    for char in encrypted_message:
        if char in decrypted_char_by_encrypted_char:
            decrypted_char = decrypted_char_by_encrypted_char[char]
            decrypted_message += decrypted_char
        else:
            decrypted_message += char
    return decrypted_message

def _get_decrypted_char_by_encrypted_char(chars_sorted_by_frequency, char_frequency):
    decrypted_char_by_encrypted_char = {}
    for i in range(len(chars_sorted_by_frequency)):
        encrypted_char = chars_sorted_by_frequency[i]
        decrypted_char = char_frequency[i]
        decrypted_char_by_encrypted_char[encrypted_char] = decrypted_char
    return decrypted_char_by_encrypted_char

def _get_frequency_by_char(encrypted_message):
    frequency_by_char = {}
    for char in encrypted_message:
        if char not in CHARS_TO_IGNORE:
            frequency_by_char[char] = frequency_by_char.get(char, 0) + 1
    return frequency_by_char

def _decrypt_message(encrypted_message, char_frequency):
    frequency_by_char = _get_frequency_by_char(encrypted_message)
    chars_sorted_by_frequency = sorted(frequency_by_char, key=lambda k: frequency_by_char[k], reverse=True)

    decrypted_char_by_encrypted_char = _get_decrypted_char_by_encrypted_char(chars_sorted_by_frequency, char_frequency)
    decrypted_message = _perform_decryption(encrypted_message, decrypted_char_by_encrypted_char)

    return decrypted_message

def _main():
    if (len(sys.argv) < 2):
        print "usage: python " + sys.argv[0] + " [message]"
        return

    encrypted_message = sys.argv[1]
    decrypted_message = decrypt(encrypted_message)
    print decrypted_message

if __name__ == "__main__":
    _main()
