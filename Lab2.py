def display_main_menu():
    print("display_main_menu")


def get_user_input():
    listing = []
    for i in range(7):
        numbers = float(input("Please enter a number:"))

        listing.append(numbers)

    return listing


def calc_average(numberset):
    sum = 0
    for i in range(0, 7):
        sum = sum + numberset[i]
    avg = sum / 7
    return avg


def find_min_max(numberset2):
    min_max = []
    maximum = max(numberset2)

    # finding min

    minimum = min(numberset2)

    min_max.append(minimum)
    min_max.append(maximum)
    return min_max[0], min_max[1]


def calc_median_temperature(numberset3):
    n = len(numberset3)
    s = sorted(numberset3)
    index = (n - 1) // 2

    if n % 2 == 0:
        return ( s[index] + s[index + 1]) / 2.0
    else:
        return s[index]

def main():
    display_main_menu()
    num_list = get_user_input()
    print(num_list)
    average = calc_average(num_list)
    print("The average is " + str(float(average)))
    minimum_max = find_min_max(num_list)
    minnumber = minimum_max[0]
    maxnumber = minimum_max[1]
    print("The minimum temperature is " + str(minnumber) + " and the maximum temperature "
          + str(maxnumber))
    median = calc_median_temperature(num_list)
    print("The median number is: " + str(median))


if __name__ == "__main__":
    main()