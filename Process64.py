import base64


#For Google search

def Dl_Google(GoogleString,FileName):
    s1 = GoogleString[:22]
    s2 = GoogleString[23:]
    print s1

    if "jpeg" in s1:
        FileType = "jpeg"
    elif "png" in s1:
        FileType = "png"
    else:
        pass

    if FileType is not None:
        Dl(s2,FileName,FileType)
    else:
        "can't confirm file type"

def Show_Google(GoogleString):
    s1 = GoogleString[:22]
    s2 = GoogleString[23:]
    Show(s2)


##base function

def Dl(String64,FileName,FileType):
    DecodeStr = base64.decodestring(String64)
    f = open(FileName+"."+FileType, "w")
    f.write(DecodeStr)
    f.close()


def Show(String64):
    DecodeStr = base64.decodestring(String64)
    import PIL.Image
    from io import BytesIO
    img = PIL.Image.open(BytesIO(DecodeStr))
    img.show()
