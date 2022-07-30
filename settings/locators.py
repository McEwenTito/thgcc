#Login page locators
username_input = "/html/body/div[2]/div[2]/div[4]/div/div[1]/div/div/form/fieldset/div[1]/div/input"
password_input = "/html/body/div[2]/div[2]/div[4]/div/div[1]/div/div/form/fieldset/div[2]/div/input"
privacy_checkbox = "/html/body/div[2]/div[2]/div[4]/div/div[1]/div/div/form/fieldset/div[3]/div/label/input"
login_button = "/html/body/div[2]/div[2]/div[4]/div/div[1]/div/div/form/fieldset/div[3]/div/input"

#TODO: Use a more dynamic locator
book_tee_time_link = "/html/body/div[2]/div[2]/div[4]/div/div/div[2]/div[4]/table/tbody/tr[2]/td/a"
accept_code_button = "/html/body/div[2]/div/form/section/div/div/div[1]/a"


#calender page locators
calender_dropdown = "/html/body/div[2]/div[2]/div[4]/div/div[2]/form/div[1]/p/img"
calender_dropdown = "/html/body/div[2]/div[2]/div[4]/div/div[2]/form/div[1]/p/input[1]"
# sundays = "/html/body/div[4]/table/tbody/tr/td[7]"
sundays = "/html/body/div[4]/table/tbody/tr/td/a/.."
next = "/html/body/div[4]/div/a[2]"

days = {
    "saturdays": "/html/body/div[4]/table/tbody/tr/td[6]",
    "sundays": "/html/body/div[4]/table/tbody/tr/td[7]"
}


available_slot = "/html/body/div[2]/div[2]/div[4]/div/div[2]/div/table/tbody/tr/td[1]/a"
submit_slot = "/html/body/div[6]/div[7]/div/div[2]/form/input[6]"
add_player = "/html/body/div[2]/div[2]/div[4]/div/div/div[1]/div[2]/div/table/tbody/tr/td[2]/i/a"
# add_player = "/html/body/div[2]/div[2]/div[4]/div/div[2]/div[1]/div[2]/div/table/tbody/tr[2]/td[2]/i/a"
another_member = "/html/body/div[5]/div/table/tbody/tr[2]/td[2]/div/div/a[1]"
player_input = "/html/body/div[5]/div/table/tbody/tr[2]/td[2]/div/span[1]/form/input[1]"
submit_player = "/html/body/div[5]/div/table/tbody/tr[2]/td[2]/div/span[1]/form/input[2]"
finish = "/html/body/div[2]/div[2]/div[4]/div/div[2]/a"