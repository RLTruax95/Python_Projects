import random

def main():
    num_birthdays = int(input("How many birthdays would you like to generate? "))
    sim_count = int(input("How many simulations would you like to run? "))
    total_duplicates = 0

    for i in range(sim_count):
        birthday_list = generate_birthdays(num_birthdays)
        total_duplicates += check_birthdays(num_birthdays, birthday_list)
        if i % (sim_count/10) == 0:
            print(f"Running simulation #{i}")

    # percent = calculate_percent()
    print(f"\nTotal duplicate numbers: {total_duplicates}")
    print(f"Out of {sim_count} simulations of {num_birthdays} birthdays each, there is a "
          f"{calculate_percent(total_duplicates, sim_count)}% chance of there being a duplicate birthday")
#####################################################################
#Generates the list of birthdays
def generate_birthdays(num_birthdays):
    birthdays = []
    for  i in range(num_birthdays):
        birthdays.append(random.randint(0, 364))
    return birthdays
#####################################################################
#Checks to see if there is a duplicate birthday among the birthdays
def check_birthdays(num_birthdays, birthdays):
    while len(birthdays) > 0:
        temp = birthdays.pop()
        if temp in birthdays:
            return 1
    return 0
#####################################################################
#Caluates the percent chance of the duplicates over all simulations
def calculate_percent(duplicates, sim):
    return 100 * duplicates / sim

if __name__ == '__main__':
    main()