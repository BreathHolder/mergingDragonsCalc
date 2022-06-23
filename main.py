def down_conversion(widgets_needed):
    group_5 = 0
    group_3 = 0
    if widgets_needed % 2 == 0:
        while widgets_needed > 0:
            group_5 += 1
            widgets_needed -= 2
    else:
        widgets_needed -= 1
        group_3 += 1
        while widgets_needed > 0:
            group_5 += 1
            widgets_needed -= 2
    print("you need " + str(group_3) + " groups of 3 and " + str(group_5) + " groups of 5.")
    return (group_3 * 3) + (group_5 * 5)

def down_conversion_multi_level(widgets_needed, level):
    print("let's start moving down the levels. You are starting on Level " + str(level))
    if level > 1:
        while level > 1:
            widgets_needed = down_conversion(widgets_needed)
            level -= 1
            print("at level " + str(level) + " you will need " + str(widgets_needed))
    else:
        return "you need to select a level"
    return widgets_needed

def down_conversion_multi_level(widgets_needed, end_level, start_level):
    print("you are trying to get " + str(widgets_needed) + " baubles on level " + str(end_level))
    if end_level > 1:
        while end_level > start_level:
            widgets_needed = down_conversion(widgets_needed)
            end_level -= 1
            print("at level " + str(end_level) + " you will need " + str(widgets_needed))
    else:
        return "you need to select a level"
    return widgets_needed

print(down_conversion_multi_level(5, 9, 4))