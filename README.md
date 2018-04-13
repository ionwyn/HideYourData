## HYD (Hide Your Data)

Image Steganography built with Python 3.6 and PyQt5 inspired by the Computerphile video below (click link to view video):

<a href="http://www.youtube.com/watch?feature=player_embedded&v=TWEXCYQKyDc
" target="_blank"><img src="http://img.youtube.com/vi/TWEXCYQKyDc/0.jpg" 
alt="IMAGE ALT TEXT HERE" width="240" height="180" border="10" /></a>

## Usage
Download hydExe as .zip, extract it, head to /dist/hyd/ and run hyd.exe

WARNING:  Only upload PNG image (JPEG is lossy and it won't work).  Only upload .txt file for hiding.  This is unstable version.

Click Encrypt, upload your PNG, upload your .txt, and click the Encrypt button

Click Decrypt, upload the PNG with hidden stuff, hit Decrypt.

I apologize for the improper terminologies used, here.  I know what I have currently isn't an Encryption/Decryption system, but this is because future goal is dedicated to implement Compression followed by Encryption before Steganography.

## Development setup

Don't download hydExe

Install requirements:

```sh
pip install -r requirements.txt
```

Add the following code to the bottom of LSteg.py:

```python
def main():
    args = docopt.docopt(__doc__, version="0.2")
    in_f = args["--in"]
    out_f = args["--out"]
    in_img = cv2.imread(in_f)
    steg = LSBSteg(in_img)

    if args['encode']:
        data = open(args["--file"], "rb").read()
        res = steg.encode_binary(data)
        cv2.imwrite(out_f, res)

    elif args["decode"]:
        raw = steg.decode_binary()
        with open(out_f, "wb") as f:
            f.write(raw)


if __name__=="__main__":
    main()
```

```sh
Usage:
  LSBSteg.py encode -i <inputImage in PNG format> -o <newImage.png> -f <file>
  LSBSteg.py decode -i <inputImageWithHiddenStuff.PNG> -o <output.txt>
```

## Future work

In folder Encryption_AES is a code for AES 256 Encryption in CBC mode with #PKCS7 padding.  This will be used in the future releases.  The reason why I don't use it... well, honestly... because I am bad with bit processing stuff.

The AES in crypt.py is not to be confused with AES implementation I did with [Grazietta](https://github.com/grazietta).

Future work also includes allowing users to hide any file they want (though in practice this is done already through using bin file format)

Better UI?  No thanks.

## Contributing

Don't.  Just don't do it.  I got this.  Unless you're [Yassine](https://github.com/yasster).
