def solution(n, w, num):
    top = (n-1)//w+1
    row = (num-1)//w+1
    col = (num-1)%w
    top_col = (n-1)%w
    if top%2==row%2:
        return top-row + (0 if top_col<col else 1)
    else:
        return top-row + (0 if top_col+col<w-1 else 1) 
