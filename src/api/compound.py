from flask import Blueprint, render_template, request, jsonify
from src.functions.compound_interest import calculate_compound_interest

# Blueprint Configuration
compound_bp = Blueprint(
    'compound_bp', __name__
)

@compound_bp.route("/compound_interest", methods=['GET'])
def compound():
    query_params = request.args

    initial_balance = int(query_params.get('initial_balance'))
    interest_rate = int(query_params.get('interest_rate'))
    monthly_input = int(query_params.get('monthly_input'))
    months = int(query_params.get('months'))

    return jsonify(calculate_compound_interest(    
        initial_balance,
        interest_rate,
        monthly_input,
        months
    ))