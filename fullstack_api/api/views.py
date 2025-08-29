from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def bfhl(request):
    try:
        data = request.data.get("data", [])
        od, ev, alpha, sp = [], [], [], []
        s = 0

        for i in data:
            if i.isdigit():
                n = int(i)
                (ev if n % 2 == 0 else od).append(i)
                s += n
            elif i.isalpha():
                alpha.append(i.upper())
            else:
                sp.append(i)

        rev_alpha = "".join(alpha)[::-1]
        concat = "".join([c.upper() if idx % 2 == 0 else c.lower() for idx, c in enumerate(rev_alpha)])

        res = {
            "is_success": True,
            "user_id": "john_doe_17091999",
            "email": "john@xyz.com",
            "roll_number": "ABCD123",
            "odd_numbers": od,
            "even_numbers": ev,
            "alphabets": alpha,
            "special_characters": sp,
            "sum": str(s),
            "concat_string": concat
        }
        return Response(res, status=200)

    except Exception as e:
        return Response({"is_success": False, "error": str(e)}, status=400)
