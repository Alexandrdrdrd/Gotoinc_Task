def encrypt(text, n):
    if text == "" or n <= 0:
        return text
    for i in range(n):
        text = text[1::2] + text[::2]
    return text.lower()


def decrypt(encrypted_text, n):
    if encrypted_text == "" or n <= 0:
        return encrypted_text
    l = []
    l1 = []
    for i in encrypted_text:
        l1.append(i)

    for i in range(n):
        l = []
        for j in range(int(len(encrypted_text) / 2)):
            l.append(l1[j + int((len(encrypted_text) / 2))])
            l.append(l1[j])
        l1 = l

    return "".join(l)
