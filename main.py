from bot import Bot

def main():
    bot = Bot(contract_addr="0x27ae27110350b98d564b9a3eed31baebc82d878d")
    bot.print_contract_total_supply()
    #bot.run()

if __name__ == "__main__":
    main()