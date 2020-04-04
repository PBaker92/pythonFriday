#establish variables
total_bill = int(input('Total bill amount? '))
level_of_service = input('Level of service? Good, Fair, Bad')
split_how_many = int(input('Split how many ways? '))

tip_text = 'Tip amount: '
tip = 0.0

total_text = 'Total amount: '

if level_of_service == 'good':
  tip = total_bill * 0.2
elif level_of_service == 'fair':
  tip = total_bill * 0.15
elif level_of_service == 'bad':
  tip = total_bill * 0.1

grand_total = total_bill + tip
per_person = grand_total / split_how_many
per_person_text = 'Amount per person: '

print(tip_text + f'{tip:.2f}')
print(total_text + f'{grand_total:.2f}')
print(per_person_text + f'{per_person:.2f}')