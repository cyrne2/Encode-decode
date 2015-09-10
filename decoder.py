#decode to encode

def decoder():
    message = raw_input("Please enter your message:")
    length = len(message) #message length
    d = list(message) #changes message to a list
    #we then need to change letters into numbers so they can be changed in the cipher
    #Use ASCII table and use the function ord("")
    e = [0]*int(length) #this is a zero array times the length of the first array
    f = [0]*int(length)
    g = [0]*int(length)
    #Need to use for loop so the function goes through each part of the message and does the
    # same thing to each letter
    #Step one: convert letters in message into numbers
    for i in range (0, int(length)):
        e[i] = ord(d[i])
    #Step two: Add 4 to the numbers
    for k in range (0, int(length)):
        f[k] = e[k]- 4      
    #Step three: convert back the numbers into letters
    for l in range (0, int(length)):
        g[l] = chr(f[l])      
    cmess = ""
    for m in range (0, int(length)):
        cmess += (str(g[m]))
        
    print "Your coded message is: " + message
    print "Your decoded message is: " + cmess
    
    return cmess

decoder()

