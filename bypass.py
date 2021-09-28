from hcapbypass import bypass
import sys

captcha_solved = bypass(sys.argv[1], 'google.com', True)
print(captcha_solved)