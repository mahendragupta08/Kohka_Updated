import razorpay
from flask import Blueprint, request, jsonify

# Create a Blueprint for Razorpay routes
payment = Blueprint('razorpay', __name__)

# Razorpay credentials (replace with your keys)
RAZORPAY_KEY_ID = 'your_key_id'
RAZORPAY_KEY_SECRET = 'your_key_secret'

# Create Razorpay client instance
client = razorpay.Client(auth=(RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET))

@payment.route('/create_order', methods=['POST'])
def create_order():
    try:
        # Get data from the request
        data = request.json
        
        # Create an order (amount is in paise)
        order_data = {
            'amount': data['amount'] * 100,  # Rs. to Paise
            'currency': 'INR',
            'payment_capture': 1  # Automatic capture after payment
        }
        
        # Create order via Razorpay API
        order = client.order.create(data=order_data)
        
        # Return the created order details
        return jsonify({
            'order_id': order['id'],
            'amount': order['amount'],
            'currency': order['currency']
        }), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@payment.route('/verify_payment', methods=['POST'])
def verify_payment():
    try:
        # Get payment details from the request
        payment_id = request.json['razorpay_payment_id']
        order_id = request.json['razorpay_order_id']
        signature = request.json['razorpay_signature']

        # Verify payment signature
        params_dict = {
            'razorpay_order_id': order_id,
            'razorpay_payment_id': payment_id,
            'razorpay_signature': signature
        }

        # Verify signature
        client.utility.verify_payment_signature(params_dict)

        # Payment successful
        return jsonify({'message': 'Payment verified successfully'}), 200

    except razorpay.errors.SignatureVerificationError as e:
        return jsonify({'error': 'Signature verification failed'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500
