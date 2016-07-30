import InputBox
import MessageBox


def string2array(s):
    s = s.split(" ")
    for i in range(len(s)):
        s[i] = s[i].strip(',')
        s[i] = s[i].strip('.')
        s[i] = s[i].strip(':')
        s[i] = s[i].strip('!')
        s[i] = s[i].strip('-')
        s[i] = s[i].strip('\'')
        s[i] = s[i].strip('\"')
    s = set(s)
    s = list(s)
    substringcount(s)


def substringcount(s):
    msg = "\nSubstring\tFrequency\n"
    msg += "---------\t---------\n"
    for i in range(len(s)):
        c = original.count(s[i])

        msg += s[i] + '\t' + '{:10d}'.format(c) + "\n"

    MessageBox.Show(msg)


def main():

    InputBox.ShowDialog("Enter a paragraph: ")
    global original

    original = InputBox.GetInput()

    s = original.lower()

    string2array(s)

if __name__ == "__main__":
    main()
