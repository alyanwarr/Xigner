# Xigner
Xigner is a BurpSuite plugin that parses out XML sent within the HTTP request and generates valid digital signature value on the fly.

## How to use it:

1. Clone the project
2. Add your private key file(s) in "certs" folder
3. Over-ride `<example></example>` in `xigner.py` to match your desired XML message tags name
4. Over-ride `file.key` in `run.py` to point to your private key file
5. Add `xigner.py` to your BurpSuite Project

You should now have a new tab in your BurpSuite HTTP message editor named "Signed XML" that would automatically sign and replace the original XML messages on the fly each time you click on it.

## Requirements:

1. [xmldsig](https://github.com/AntagonistHQ/xmldsig) installed
2. Jython imported in BurpSuite

## Screenshots:

![screenshot_7](https://user-images.githubusercontent.com/12968456/42410840-163b84a4-81f1-11e8-8c79-4d1792a82b46.png)


![screenshot_8](https://user-images.githubusercontent.com/12968456/42410850-3ee11b1c-81f1-11e8-91c4-debe2cccb2ad.png)


![screenshot_9](https://user-images.githubusercontent.com/12968456/42410854-44f5b8d2-81f1-11e8-92b1-a2388618320e.png)


## Credits:
AntagonistHQ for [xmldsig wrapper](https://github.com/AntagonistHQ/xmldsig)
