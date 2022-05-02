# https://leetcode.com/problems/simplify-path/

def simplify_path(path: str) -> str:
    dir_name = []

    all_items = path.split('/')

    for i in all_items:
        i = i.strip()
        if i == "..":
            if dir_name:
                dir_name.pop()
        elif i and i != ".":
            dir_name.append(i)

    res_str = ""

    for i in dir_name:
        res_str += f"/{i}"

    if res_str:
        return res_str
    else:
        return "/"


print(simplify_path("/home/"))
