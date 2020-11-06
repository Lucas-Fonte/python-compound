
def calculate_compound_interest(initial_balance, interest_rate, monthly_input, months):
    pointer = 0
    final_amount = initial_balance

    while pointer < months:
        current_final_amount = final_amount + monthly_input
        interest_rate_multiplier = calculate_interest_rate_multiplier(interest_rate)

        final_amount = current_final_amount * interest_rate_multiplier

        pointer += 1

    return {
        'initial_balance': initial_balance,
        'interest_rate': f'{interest_rate}%',
        'monthly_input': monthly_input,
        'months': months,
        'final_amount': round(final_amount, 2),
    }


def calculate_interest_rate_multiplier(interest_rate):
    return 1 + (interest_rate / 100)