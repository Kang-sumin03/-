def get_integer(prompt):
    while True:
        try:
            amount = int(input(prompt))
            if amount >= 0:
                return amount
            else:
                print("금액은 0 이상의 정수여야 합니다. 다시 입력해주세요.")
        except ValueError:
            print("잘못된 입력입니다. 정수만 입력해주세요.")

amount = get_integer("동전으로 교환하고자 하는 금액은? ")

def exchange(amount):
    n500 = amount // 500
    amount = amount % 500

    n100 = amount // 100
    amount = amount % 100

    n50 = amount // 50
    amount = amount % 50

    n10 = amount // 10
    amount = amount % 10

    print("500원 동전의 개수 : " + str(n500))
    print("100원 동전의 개수 : " + str(n100))
    print("50원 동전의 개수 : " + str(n50))
    print("10원 동전의 개수 : " + str(n10))


exchange(amount)
