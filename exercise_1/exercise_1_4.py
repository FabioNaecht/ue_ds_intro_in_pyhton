def gauss_easter_equation(year: int) -> int:
    K = year // 100
    M = 15 + (3 * K + 3) // 4 - (8 * K + 13) // 25
    S = 2 - (3 * K + 3) // 4
    A = year % 19
    D = (19 * A + M) % 30
    R = (D + A // 11) // 29
    OG = 21 + D - R
    SZ = 7 - (year + year // 4 + S) % 7
    OE = 7 - (OG - SZ) % 7
    OS = OG + OE
    return OS


if __name__ == '__main__':
    year1 = 1984
    print(f"Ostersonntag {year1}: {gauss_easter_equation(year1)}")

    year2 = 2005
    print(f"Ostersonntag {year2}: {gauss_easter_equation(year2)}")

    year3 = 2023
    print(f"Ostersonntag {year3}: {gauss_easter_equation(year3)}")

