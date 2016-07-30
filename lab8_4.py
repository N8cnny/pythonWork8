import InputBox
import MessageBox

s = "Result:\n"


def acct2number():
    InputBox.ShowDialog("Enter the dollar amount: ")
    amt = InputBox.GetInput()

    global s

    s += "Acct to number: "
    for i in range(len(amt)):
        if amt[i] == '$':
            pass
        elif amt[i] == ',':
            pass
        else:
            s = s + amt[i]
    s += "\n"


def number2acct():
    global s
    s += "Number to Acct: "

    InputBox.ShowDialog("Enter a large number: ")
    x = InputBox.GetInput()
    s += '${:,.2f}'.format(float(x)) + "\n"


def number2acct2():
    InputBox.ShowDialog("Enter a large number: ")
    x = InputBox.GetInput()

    x = '{:.2f}'.format(float(x))
    result = "$" + x
    x = x.split('.')

    if len(x[0]) > 4:
        result = ''
        x1 = x[0]

    n = len(x[0]) // 4
    for i in range(n):
        if i == (n-1):
            result = "$" + x1[-5-(i*4):-1-(i*4)] + result
        else:
            result = "," + x1[-5-(i*4):-1-(i*4)] + result
            result = result + "." + x[1]
    global s

    s += "Number to acct 2: "
    s += result + "\n"


def main():
    acct2number()
    number2acct()
    number2acct2()

    MessageBox.Show(s)

if __name__ == "__main__":
    main()
