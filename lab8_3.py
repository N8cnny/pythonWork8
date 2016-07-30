import MessageBox


def tuple2string(tuple):
    s = ''
    for i in range(len(tuple)):
        s = s + tuple[i] + " "
    s = s.replace(' .', '.')
    s = s.replace(' ,', ',')
    return s


def list2string(list):
    s = ''
    for i in range(len(list)):
        s = s + list[i] + " "
    s = s.replace(' .', '.')
    s = s.replace(' ,', ',')
    return s


def dictkey2string(dict):
    k = list(dict.keys())
    s = ''
    for i in range(len(k)):
        s = s + str(k[i]) + " "
    return s


def dictvalue2string(dict):
    v = list(dict.values())
    s = ''
    for i in range(len(v)):
        s = s + str(v[i]) + " "
    return s


def main():
    t = ('Life', 'is', 'a', 'journey', '.', 'Time', 'is', 'a', 'river', '.')

    l = ["Look", "in", "the", "mirror", "to", "meet", "your", "true", "energy", ",",
         "lover", ",", "and", "friend", "."]

    wd = {
     "Mon": 'pork',
     "Tue": 'chicken',
     "Wed": 'tuna',
     "Thu": 'burger',
     "Fri": 'sushi',
     "Sat": 'soup',
     "Sun": 'salad'
    }

    result = tuple2string(t) + "\n"
    result += list2string(l) + "\n"
    result += dictkey2string(wd) + "\n"
    result += dictvalue2string(wd) + "\n"

    MessageBox.Show(result)
if __name__ == "__main__":
    main()
