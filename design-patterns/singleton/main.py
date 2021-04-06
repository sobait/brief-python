from connection import Connection


def main():
    my_connection1 = Connection()
    my_connection2 = Connection()
    print(my_connection1)
    print(my_connection2)
    print(f"my_connection1 is my_connection2 ? {my_connection1 is my_connection2}")


if __name__ == "__main__":
    main()