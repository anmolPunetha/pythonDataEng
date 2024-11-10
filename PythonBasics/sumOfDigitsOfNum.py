a = 123.45
a_str = str(a)
nums = a_str.split('.')

new_no = nums[0] # a string
if len(nums)>1:
    new_no+=nums[1]

final_int_no = int(new_no)
ans = 0
while final_int_no>0:
    digit = final_int_no % 10
    ans+=digit
    final_int_no = final_int_no//10

print(ans)
    
