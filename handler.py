import json

USER_ID = "pratishtha_16072004"
EMAIL = "pratishtha1607@gmail.com"
ROLL_NUMBER = "22BCE1439"

def alternating_caps(s):
    result = []
    upper = True
    for ch in s[::-1]:  # reverse
        if upper:
            result.append(ch.upper())
        else:
            result.append(ch.lower())
        upper = not upper
    return "".join(result)

def process(event, context):
    try:
        body = json.loads(event.get("body", "{}"))
        data = body['data']

        evens, odds, alphabets, alphabets_up, special_chars = [], [], [], [], []
        num_sum = 0

        for item in data:
            if item.isdigit(): 
                num = int(item)
                num_sum += num
                if num % 2 == 0:
                    evens.append(item)
                else:
                    odds.append(item)
            elif item.isalpha():  
                alphabets.append(item)
                alphabets_up.append(item.upper())
            else:  
                special_chars.append(item)

        alternate = alternating_caps("".join(alphabets))


        response = {
            "is_success":True,
            "user_id":USER_ID,
            "email": EMAIL,
            "roll_number": ROLL_NUMBER,
            "odd_numbers": odds,
            "even_numbers": evens,
            "alphabets": alphabets_up,
            "special_characters": special_chars,
            "sum": str(num_sum),
            "concat_string": alternate
        }

        return {
            "statusCode": 200,
            "body": json.dumps(response)
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"is_success": False, "error": str(e)})
        }
