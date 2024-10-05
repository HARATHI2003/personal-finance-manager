from database import create_connection

def generate_report(user_id, period='monthly'):

    conn = create_connection()
    cursor = conn.cursor()

    if period == 'monthly':
        query = '''
            SELECT SUM(amount) FROM transactions WHERE user_id = ? AND date LIKE '2024-10%'
        '''
    elif period == 'yearly':
        query = '''
            SELECT SUM(amount) FROM transactions WHERE user_id = ? AND date LIKE '2024%'
        '''

    cursor.execute(query, (user_id,))
    result = cursor.fetchone()
    
    # Handle cases where no transactions exist
    total = result[0] if result and result[0] is not None else 0.0

    conn.close()
    return total
