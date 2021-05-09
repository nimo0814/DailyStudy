"""
目的：编写一个Python脚本，可以从邮件地址中获取用户名和域名。
"""

email=input("What is your email address?:").strip()
user_name=email[:email.index("@")]
domain_name=email[email.index("@")+1:]
res=f"Your username is '{user_name}' and your domain name is '{domain_name}'"
print(res)
