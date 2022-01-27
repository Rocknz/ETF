import yfinance as yf

from GoogleDrive import GoogleDrive


def main():
    google_drive = GoogleDrive()

    with open("output_ETF.csv", "w", encoding="utf-8") as fp:
        ticker_column = 'C'
        ticker_row = 1
        position = ticker_column + str(ticker_row)
        ticker_cnt = int(google_drive.read(position))
        ticker_name_list = []
        for i in range(ticker_cnt):
            ticker_row += 1
            position = ticker_column + str(ticker_row)
            ticker_name = str(google_drive.read(position))
            ticker_name_list.append(ticker_name)

        column = 'C'
        row = 15

        for ticker_name in ticker_name_list:
            print(ticker_name)
            str_val = ticker_name

            ticker = yf.Ticker(ticker_name)
            val = ticker.info.get("regularMarketPrice")

            position = column + str(row)
            google_drive.update(position, val)

            str_val += "," + str(val)

            row += 1
            fp.write(str_val)
            fp.write("\n")

    fp.close()


if __name__ == "__main__":
    main()
