from coinacceptor import coinacceptor
def main():
    acceptor = coinacceptor()
    print("program starting.")
    print("welcome to coin acceptor program.")
    print("insert coins by typing it's value (0 returns the money, -1 exits the program)")

    while True:
        try:
            coin_value = float(input("insert coin(0 return, -1 exit):"))
            if coin_value == -1:
               print("exiting program.")
               print("thank you for using the program.")
               print("program ending")
               break
            elif coin_value == 0:
               returned_amount, returned_value = acceptor.returncoins()
               print(f"{returned_amount} coins with {returned_value}euros values returned.")
               print("inserted coins = 0, value = 0 euros ")
            elif coin_value > 0:
               acceptor.insertcoin(coin_value)
               print(f"inserted coins = {acceptor.getamount()}, value = {acceptor.getvalue()} euros")
            else:
                print("invalid input, please insert a valid coin value (0 return, -1 exit)")
        except ValueError:
            print("invalid input, please insert a valid coin value (0 return, -1 exit)")

if __name__ == "__main__":
    main()
                  