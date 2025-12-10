def can_join_club(age: int, balance: int) -> bool:
    # Checks if a visitor is allowed to enter the club
    return 20 <= age <= 40 and balance >= 100


if __name__ == '__main__':
    age, balance = map(int, input().split())
    print(can_join_club(age, balance))