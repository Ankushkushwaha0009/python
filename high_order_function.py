# high order function = a function that either:
#                      1.accept a function as an argument 
#                      or
#                      2.return a function
#                      (in pyhton functions are also treated as objects)
def loud(text):
    return text.upper()
def quiet(text):
    return text.lower()
def hello(func):
    text = func("hi Ankush")
    print(text)

hello(loud)  # pasiing whole function
hello(quiet) # passing the whole function




#--------------------------------

# def divisor(x):
#     def dividend(y):
#         return y/x
#     return dividend   returning a function here 

# divide = divisor(2)
# print(divide(10))










