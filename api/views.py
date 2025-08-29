from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

FULL_NAME = "john_doe"
DOB = "17091999"
EMAIL = "john@xyz.com"
ROLL_NUMBER = "ABCD123"

@csrf_exempt
def bfhl(request):
    if request.method == "POST":
        try:
            body = json.loads(request.body.decode("utf-8"))
            arr = body.get("data", [])

            evens, odds, alphabets, specials = [], [], [], []
            total_sum = 0

            for item in arr:
                if item.isdigit():
                    num = int(item)
                    if num % 2 == 0:
                        evens.append(item)
                    else:
                        odds.append(item)
                    total_sum += num
                elif item.isalpha():
                    alphabets.append(item.upper())
                else:
                    specials.append(item)

            only_alpha = "".join([ch for ch in "".join(arr) if ch.isalpha()])
            rev = only_alpha[::-1]
            concat_string = "".join(
                [ch.upper() if i % 2 == 0 else ch.lower() for i, ch in enumerate(rev)]
            )

            response = {
                "is_success": True,
                "user_id": f"{FULL_NAME.lower()}_{DOB}",
                "email": EMAIL,
                "roll_number": ROLL_NUMBER,
                "odd_numbers": odds,
                "even_numbers": evens,
                "alphabets": alphabets,
                "special_characters": specials,
                "sum": str(total_sum),
                "concat_string": concat_string,
            }
            return JsonResponse(response, status=200)
        except Exception as e:
            return JsonResponse({"is_success": False, "error": str(e)}, status=400)
    return JsonResponse({"is_success": False, "error": "Invalid method"}, status=405)
