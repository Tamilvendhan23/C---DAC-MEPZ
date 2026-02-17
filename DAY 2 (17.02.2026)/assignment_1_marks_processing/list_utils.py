# 1.1 Function: Get Top N Marks
def get_top_n_marks(marks,n):
    if not type(marks)==list:
        raise TypeError("Entered value is not valid!!")
    if not (n>0):
        raise ValueError("Value must be positve!!")
    srt=sorted(marks)
    return srt[n:]
    


