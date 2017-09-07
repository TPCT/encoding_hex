def encoding(string='', key=0):
    return "".join([str(hex(ord(i)+key+10)).replace("0x",'') for i in bytearray(string,"utf-8").hex()])
def decoding(string='', key=0):
    return bytearray.fromhex(bytearray.fromhex("".join([str(hex(ord(i)-key-10)).replace("0x",'') for i in bytearray.fromhex(string).decode()])).decode()).decode()
    
