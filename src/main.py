from functions import get_data, get_sort_data, get_format_data, get_filter_data


def main():
    data = get_format_data(get_sort_data(get_filter_data(get_data())))
    for value in data:
        print(value, end='\n\n')


if __name__ == "__main__":
    main()
