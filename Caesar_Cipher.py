
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

cont = "yes"

while cont == "yes":

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 25


    def encode(t=text):
        encode_text = []

        for harf in text:

            if harf in alphabet:

                alpha_order = alphabet.index(harf)
                encode_order = alpha_order + shift

                if encode_order > 25:
                    encode_order -= 26

                encode_text += alphabet[encode_order]

            else:
                encode_text += harf

        output = ''.join(encode_text)
        print(f"Encoded text: {output}")


    def decode(t=text):
        decode_text = []

        for harf in text:

            if harf in alphabet:

                alph_order = alphabet.index(harf)
                decode_order = alph_order - shift

                decode_text += alphabet[decode_order]

            else:
                decode_text += harf

        output = ''.join(decode_text)
        print(f"Decoded text: {output}")


    if direction == "encode":
        encode(text)

    elif direction == "decode":
        decode(text)

    cont = str(input("Type 'yes' if you want to go again. Otherwise type 'no'. \n")).lower()




