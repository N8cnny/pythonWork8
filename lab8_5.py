import InputBox
import MessageBox

s = "Result:\n"


def ipv4_binary(ipaddr):

    s = ipaddr
    s = s.split('.')
    for i in range(len(s)):
        s[i] = bin(int(s[i]))
        s[i] = s[i].replace('0b', '')
    for i in range(len(s)):
        if len(s[i]) == 8:
            pass
        else:
            n = 8 - len(s[i])
            for j in range(n):
                s[i] = '0' + s[i]

    x = '.'
    s = x.join(s)
    return s


def ipv6(ip):

    s = ip.split('.')
    ipv6 = ""
    for i in s:
        if i == s[1]:
            ipv6 = ipv6 + tohex(i) + ":"
        else:
            ipv6 = ipv6 + tohex(i)
    ipv6 = "0:0:0:0:0:ffff:" + ipv6
    return ipv6


def tohex(s):
    s = hex(int(s))
    s1 = s[2:]

    if len(s1) == 1:
        s1 = "0" + s1

    return s1


def main():
    InputBox.ShowDialog("Enter a valid IPv4 address: ")
    ipaddr = InputBox.GetInput()

    s = "Result:\n"
    s += "IPv6 in Hex: " + ipv6(ipaddr) + "\n"
    s += "IPv6 in Binary: " + ipv4_binary(ipaddr) + "\n"


    MessageBox.Show(s)

if __name__ == "__main__":
    main()

