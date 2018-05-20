import os
import sys
import zipfile
import codecs


def valid_encoding(enc):
    try:
        codecs.lookup(enc)
    except LookupError:
        return False
    return True


def proc(zfile, encoding, passwd):
    with zipfile.ZipFile(zfile) as zipf:
        for info in zipf.infolist():
            if info.is_dir():
                dirname = info.filename.encode('cp437').decode(encoding)
                os.mkdir(dirname)
            else:
                dirname, basename = info.filename.encode('cp437').decode(encoding).rsplit("/", 1)
                # zipf.extract(info, newname, passwd)  # this doesn't work
                with open(os.path.join(dirname, basename), 'wb') as f:
                    f.write(zipf.read(info, passwd))


if "__main__" == __name__:
    if len(sys.argv) < 3:
        exit("usage: %s zipfile encoding" % sys.argv[0])
    if not zipfile.is_zipfile(sys.argv[1]):
        exit("%s is not a zipfile." % sys.argv[1])
    if not valid_encoding(sys.argv[2]):
        exit("encoding %s is not valid." % sys.argv[2])
    if len(sys.argv) > 3:
        passwd = sys.argv[3]
    else:
        passwd = None

    proc(sys.argv[1], sys.argv[2], passwd)
