import InputBox
import MessageBox


def reverseit(s):
    s1 = s
    s2 = ""
    for i in range(len(s1)-1, -1, -1):
        s2 = s2 + s1[i]
    return "reverse: " + (s2 * 2)


def backwardindex(s):
    s1 = ''
    for i in range(1, len(s)+1):
        s1 = s1 + s[-i] + " "
    return "backward: " + s1


def multipleformat(s):
    s1 = "upper: " + s.upper() + "\n"
    s1 += "lower: " + s.lower() + "\n"
    s1 += "capitalize: " + s.capitalize() + "\n"
    s1 += "title: " + s.title() + "\n"
    return s1


def replaceit(s):
    s = s.split()
    for i in range(len(s)):
        s[i] = "<i>" + s[i] + "</i>"
    return str(s)


def main():

    InputBox.ShowDialog("Enter a sentence: ")
    s = InputBox.GetInput()

    result = reverseit(s) + "\n"
    result += backwardindex(s) + "\n"
    result += multipleformat(s) + "\n"
    result += replaceit(s) + "\n"

    MessageBox.Show(result)

if __name__ == "__main__":
    main()
