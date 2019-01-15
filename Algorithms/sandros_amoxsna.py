def decode(s):

   i = 0

   def _decode():

       nonlocal i, s

       ans = ""

       n = len(s)

       while i < n:
           if s[i].isdigit():
               if s[i + 1] == '[':
                   p = i
                   i += 2
                   x = _decode()
                   ans += int(s[p]) * x
               else:
                   ans += int(s[i]) * s[i + 1]
                   i += 1
           elif s[i] == ']':
               break
           else:
               ans += s[i]
           i += 1
       return ans

   return _decode()


assert decode("sandro") == "sandro"
assert decode("3a4b") == "aaabbbb"
assert decode("a2bc3[a2bc4[a2d]c]d6g") == "abbcabbcaddaddaddaddcabbcaddaddaddaddcabbcaddaddaddaddcdgggggg"
assert decode("") == ""
assert decode("a") == "a"
assert decode("1[1[1[b]]]") == "b"
assert decode("1[1[1[bc1[d]e2[fg]g]]]") == "bcdefgfgg"