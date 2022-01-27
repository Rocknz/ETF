import yfinance as yf

from GoogleDrive import GoogleDrive


def main():
    google_drive = GoogleDrive()

    with open("output_ETF.csv", "w", encoding="utf-8") as fp:
        ticker_name_list = ['VOO', 'IEF', 'TLT', 'IAU', 'PDBC']
        asset_cnt = [1, 1, 1, 1, 1]
        column = 'B'
        row = 15
        for asset in asset_cnt:
            position = column + str(row)
            row += 1
            google_drive.update(position, asset)

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
