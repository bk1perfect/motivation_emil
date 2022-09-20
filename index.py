import smtplib
import datetime as dt
import random


MY_EMAIL = "abhishekbhagwat2017@gmail.com"
MY_PASSWORD = "my_password"
RECEVIER_MAIL = "bhagwat25021996@gmail.com"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 1:
    with open("C:/Studies/Study/python_programming/100_Day_Python/Day_32_to_35/86_Motivation_send/quotes.txt", "r") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
        
    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=RECEVIER_MAIL,
            msg=f"Subject: Monday Motivation\n\n{quote}"
            )