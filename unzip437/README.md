## unzip437

If you're are Windows and you receive a zip file that, after extraction, creates files with weird names, this tool is for you.

(On Linux, you can specify encoding on command line: unzip -O cp936 file.zip)

Usage:

    python3 unzip437.py zipfile encoding

You must specify the encoding, if you don't know, you have to guess.

Example:

    python3 unzip437.py f.zip gb2312   

Try gbk, gb18030 if gb2312 doesn't work.

Why does a zipfile create wrong filenames?  What happens is that when a user create a zip file, he did it in localized Windows(I think only zip on Windows has this problem) that use a specific codepages, such as cp936(Chinese), cp737(Greek), windows-1255(Hebrew), etc.  The compression tool he used, such as WinZip, treats each byte as one character using codepage [IBM437](https://en.wikipedia.org/wiki/Code_page_437). Codepage 437 is the original extened ASCII, in codepage 437, each character is 1 Byte (8 bits) and can have value from 0 to 255.  When you get the zipfile and decompress it. it produces IBM437 filenames.

In unzip437.py, we intercept the filename and encode it with `cp437` (or `ibm437`), this give up back the raw bytes of original filename.  We then decode using original encoding, such as cp936, which gives us correct unicode filename.

