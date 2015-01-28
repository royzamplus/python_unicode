#!/usr/bin/env python
# -*- coding: utf-8 -*-

def python2xStrToUnicode():
    strUtf8 = """1.此处是UTF-8编码的中文字符（之所以不是其他编码，是因为我们此处文件开头指定了是UTF-8，
                   并且此Python文件本身也是以UTF-8编码保存的，这样才能确保Python解析器，正确解析本文件，及其所包含的字符）；
                 2.接下来将要演示的是，将此段UTF-8的中文字符，解码为对应的Unicode字符；
                 3.然后输出到windows的cmd中（其中unicode字符在输出打印时，会自动转换为对应的（此处的GBK）编码的）；
    """
    print "type(strUtf8)=", type(strUtf8)    #type(strUtf8)= <type 'str'>
    decodedUnicode = strUtf8.decode("UTF-8")
    print "Decoded unicode = %s" % decodedUnicode

if __name__=="__main__":
    python2xStrToUnicode()