import base64
#------start encode -------#
def encode():
    data_to_encode = input("Ahh really quick!! : ")
    string_byts = data_to_encode.encode('utf-8')
    string_encode = base64.b64encode(string_byts)
    # (b'aztqZnNkZmRz') like this i mean
    string_without_b = string_encode.decode('utf-8')
    print(string_without_b)
#------end encode -------#

#------start decode -------#
def decode():
    data_to_decode = str(input("You again i said in need sleep!!: "))
    decodes_data = base64.b64decode(data_to_decode)
    string_without_b2 = decodes_data.decode()
    print(string_without_b2)
#------end decode -------#
x = True
while x == True:
    ask_user = str(input("encode or decode ? type (help) for more info: "))
    if ask_user == "encode":
        encode()
    elif ask_user == "stop":
        x = False
        break
    elif ask_user == "help":
        print("type (stop) exit this script, type (decode) to decode the data , type (encode) to encode data ")
    elif ask_user == "decode":
        decode()
    else:
        print("pls try again !!")



